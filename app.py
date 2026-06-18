import streamlit as st
from groq import Groq
import requests
import json
import re
import io
import time
from pypdf import PdfReader


st.set_page_config(
    page_title="FactCheck Agent",
    page_icon="🔍",
    layout="wide"
)


MODEL = "llama-3.3-70b-versatile"


# ---------------- PDF TEXT ----------------

def extract_text_from_pdf(uploaded_file):

    reader = PdfReader(
        io.BytesIO(uploaded_file.read())
    )

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text



# ---------------- GROQ ----------------

def ask_groq(prompt, api_key):

    client = Groq(
        api_key=api_key
    )


    response = client.chat.completions.create(

        model=MODEL,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0

    )


    return response.choices[0].message.content



# ---------------- CLAIM EXTRACTION ----------------

def extract_claims(text, api_key):

    prompt=f"""

Extract factual claims from the document.

Find:
- statistics
- dates
- financial figures
- technical facts

Return ONLY JSON array.

Example:

[
 {{
 "claim":"text",
 "category":"statistic"
 }}
]


DOCUMENT:

{text[:5000]}

"""


    result = ask_groq(
        prompt,
        api_key
    )


    clean = re.sub(
        r"```(json)?|```",
        "",
        result
    ).strip()


    return json.loads(clean)



# ---------------- SEARCH ----------------

def search_web(query, key):

    headers = {

        "X-API-KEY": key,

        "Content-Type": "application/json"

    }


    response = requests.post(

        "https://google.serper.dev/search",

        json={
            "q": query,
            "num": 5
        },

        headers=headers

    )


    data=response.json()


    return str(
        data.get(
            "organic",
            []
        )
    )



# ---------------- VERIFY ----------------

def verify_claim(
        claim,
        evidence,
        api_key
):


    prompt=f"""

You are a professional fact checker.

Verify the claim using evidence.


CLAIM:
{claim}


EVIDENCE:
{evidence}


Return ONLY JSON:

{{

"verdict":"Verified/Inaccurate/False/Unverifiable",

"confidence":"High/Medium/Low",

"explanation":"reason",

"real_fact":"correct fact if wrong"

}}

"""


    result = ask_groq(
        prompt,
        api_key
    )


    clean = re.sub(

        r"```(json)?|```",

        "",

        result

    ).strip()


    output=json.loads(clean)


    output["claim"]=claim


    return output




# ---------------- UI ----------------


st.title(
    "🔍 FactCheck Agent"
)


st.write(
    "PDF Claim Verification using Llama + Live Web Search"
)



# ---------------- API KEYS ----------------

groq_key = st.secrets["GROQ_API_KEY"]

serper_key = st.secrets["SERPER_API_KEY"]


pdf = st.file_uploader(

    "Upload PDF",

    type="pdf"

)



if pdf:


    if st.button(
        "Run Fact Check"
    ):


        text = extract_text_from_pdf(
            pdf
        )


        with st.spinner(
            "Extracting claims..."
        ):

            claims = extract_claims(
                text,
                groq_key
            )


        st.success(
            f"Found {len(claims)} claims"
        )



        for i, c in enumerate(claims):


            claim = c["claim"]


            st.divider()


            st.write(
                f"Checking {i+1}/{len(claims)}"
            )


            st.write(
                claim
            )


            evidence = search_web(
                claim,
                serper_key
            )


            result = verify_claim(
                claim,
                evidence,
                groq_key
            )


            verdict = result.get(
                "verdict"
            )


            if verdict == "Verified":

                st.success(
                    "✅ VERIFIED"
                )


            elif verdict == "Inaccurate":

                st.warning(
                    "⚠️ INACCURATE"
                )


            elif verdict == "False":

                st.error(
                    "❌ FALSE"
                )


            else:

                st.info(
                    "❓ UNVERIFIABLE"
                )



            st.write(
                result.get("explanation")
            )


            if result.get(
                "real_fact"
            ):

                st.info(

                    result["real_fact"]

                )


            time.sleep(.2)
