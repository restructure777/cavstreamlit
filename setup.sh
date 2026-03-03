mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"radiorock007@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
address = \"0.0.0.0\"\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
