# Field Strategy Studio pilot on Streamlit

Interactive pilot with synthetic data (HCPs, accounts, territories, calls, sales, quotas).

## Run locally
    pip install -r requirements.txt
    streamlit run app.py

## Deploy on Streamlit Community Cloud
1. Create a GitHub repository and upload these files, keeping this layout:
   - app.py
   - pilot.html
   - requirements.txt
   - .streamlit/config.toml
2. Go to share.streamlit.io, sign in with GitHub and choose New app.
3. Pick the repository, branch main and main file path app.py, then Deploy.

## Notes
- All data is generated in the browser from a fixed seed, so every viewer sees the same dataset.
- Changes users make (alignment moves, plans, inquiries, target rules) are saved in each viewer's browser only.
- For a company deployment, host the same two files on an internal Streamlit server or container.
