import streamlit as st
from openai import OpenAI

from prompts import get_prompt
from terms import show_terms

# 事前に以下の環境変数を.streamlit/secrets.tomlへ登録すること
# (必須)OPENAI_API_KEY, OPENAI_API_MODEL (任意)GITHUB_LINK, GITHUB_LOGO_URL
secrets = st.secrets.get("general", {})
OPENAI_API_KEY = secrets.get("OPENAI_API_KEY")
OPENAI_API_MODEL = secrets.get("OPENAI_API_MODEL")

if not OPENAI_API_KEY or not OPENAI_API_MODEL:
    st.error(
        "OpenAIのAPIキーまたはモデルが取得できません。環境設定を確認してください。"
    )
    st.stop()

# 初回だけインスタンスを作成し使い回す
if "openai_client" not in st.session_state:
    st.session_state.openai_client = OpenAI(api_key=OPENAI_API_KEY)


def generate_chinese_description(product_name):
    try:
        response = st.session_state.openai_client.chat.completions.create(
            model=OPENAI_API_MODEL,
            messages=[{"role": "user", "content": get_prompt(product_name)}],
        )
        return response.choices[0].message.content, None
    except Exception as e:
        return None, f"OpenAI API でエラーが発生しました: {e}"


def create_centered_column(widths=[3, 1, 3]):
    """ウィジェットを中央寄せするためのカラムを作成"""
    return st.columns(widths)[1]


st.header("中華メーカー風 商品説明ジェネレーター")

with st.form(key="input_form"):
    product_name = st.text_input("商品名称が入力するべき.今すぐ入力してください！")
    with create_centered_column():
        submitted = st.form_submit_button("生成")

if submitted:
    if product_name:
        with st.status("生成中少々待て...", expanded=True) as status:
            output_text, error = generate_chinese_description(product_name)
            if error:
                status.update(label="異常発生", state="error")
                st.write(error)
            else:
                st.subheader("商品説明")
                st.write(output_text)
                status.update(label="生成完了", state="complete")
    else:
        st.warning("⚠ 商品名称が入力ない.すぐ入力する！")

st.markdown("<br><br>", unsafe_allow_html=True)
with st.expander("利用規約", expanded=False):
    show_terms()

# GitHubリンク設置(任意)
with create_centered_column([5, 1, 5]):
    st.markdown(
        f"""
        <a href="{secrets["GITHUB_LINK"]}" target="_blank">
            <img src={secrets["GITHUB_LOGO_URL"]} width="25">
        </a>
        """,
        unsafe_allow_html=True,
    )
