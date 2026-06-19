import streamlit as st

# 設定網頁基本資訊 (改為寬版，讓履歷排版更有呼吸空間)
st.set_page_config(page_title="廖禹晴 | 音頻製作人履歷", page_icon="🎙️", layout="wide")

# 隱藏預設的選單，讓畫面保持乾淨
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# ================= 側邊欄 (Sidebar) 聯絡資訊與技能 =================
with st.sidebar:
    st.title("聯絡資訊")
    st.write("📧 yuching.audio@example.com")
    st.write("🔗 [Podcast 作品集連結](#)")
    st.write("📍 台灣 (Taiwan)")
    
    st.divider()
    
    st.title("專業技能")
    st.write("Podcast 節目企劃 🎙️")
    st.progress(95)
    st.write("人聲降噪與修復 🎛️")
    st.progress(90)
    st.write("聲音劇場混音 🎧")
    st.progress(85)
    st.write("Foley 音效製作 🎬")
    st.progress(80)
    
    st.divider()
    
    st.title("慣用軟體工具")
    # 利用 button 創造類似標籤 (Tag) 的視覺效果
    st.button("Adobe Audition", use_container_width=True)
    st.button("Logic Pro X", use_container_width=True)
    st.button("Pro Tools", use_container_width=True)
    st.button("iZotope RX (降噪神器)", use_container_width=True)

# ================= 主畫面 (Main Content) =================

# 1. Hero Section (個人簡介)
st.title("廖禹晴 (Yu-Ching)")
st.subheader("Podcast 音頻製作人 | 聲音設計師 | 金聲獎獲獎者")
st.write(
    "我是一名專注於 **Podcast 節目製作與聲音設計** 的音頻工作者。我相信「聲音是最能無防備地觸動人心的媒介」。"
    "從前期的節目企劃、訪談大綱擬定，到後期的精緻降噪、剪輯與音效混音，我致力於為聽眾打造最具沉浸感的聽覺體驗。"
)
st.divider()

# 2. 獲獎紀錄 (Awards)
st.header("🏆 獲獎紀錄")
st.success(
    "**第 XX 屆 金聲獎 (Golden Voice Awards)** \n"
    "* 🎖️ **最佳文教節目獎** —— 原創 Podcast《城市呢喃》\n"
    "* 🎖️ **最佳音效設計獎** —— 原創 Podcast《城市呢喃》"
)
st.write("<br>", unsafe_allow_html=True) # 增加一點垂直間距

# 3. 核心專案與經歷 (Experience)
st.header("💼 核心專案與經歷")

st.subheader("獨立企劃 / 錄音 / 後期混音 | 《城市呢喃》Podcast")
st.caption("2023 - 至今")
st.markdown(
    """
    * 策劃結合聲音紀錄片與訪談的原創 Podcast 節目。
    * 深入台灣各個角落採集環境音，並搭配在地人物的深度訪談。
    * 負責全集的音檔剪輯、人聲修復與聲音劇場級別的沉浸式混音設計。
    """
)
st.write("<br>", unsafe_allow_html=True)

st.subheader("音頻總監 / 剪輯師 | 商業 Podcast 頻道代工")
st.caption("2021 - 2024")
st.markdown(
    """
    * 協助超過 5 個不同領域（包含財經、心理學、生活風格）的創作者與品牌從零到一建立節目。
    * 負責制定標準錄音流程 (SOP)、片頭片尾 (Jingle) 音樂設計與版權音樂挑選。
    * 每週穩定產出高品質的母帶後期製作 (Mastering)，確保各平台收聽音量符合 LUFS 標準。
    """
)
st.divider()

# 4. 其他專業領域 (Other Expertise) - 使用兩欄排版
st.header("🌿 聲音探索與教學")
col1, col2 = st.columns(2)
with col1:
    st.info(
        "**田野錄音 (Field Recording)**\n\n"
        "遠離錄音室，熱愛帶著指向性麥克風與錄音機穿梭在山林與傳統市場間。我建立了專屬的「台灣在地聲音素材庫」，這些環境音 (Room Tone) 成為了我聲音創作中最鮮活的靈感。"
    )
with col2:
    st.warning(
        "**廣播電台與校園講師**\n\n"
        "積極參與電台節目製作人才培訓計畫，並於校園廣播社團擔任技術講師，指導學生如何運用 EQ (等化器) 與 Compressor (壓縮器) 讓自己的人聲錄音更加專業飽滿。"
    )
st.divider()

# 5. 知識庫 (Knowledge Base)
st.header("📝 聲音工程筆記")
with st.expander("如何拯救底噪過大的訪談錄音？"):
    st.markdown(
        """
        1. **基礎降噪 (Noise Reduction)：** 先採集一段 5-10 秒的純環境底噪作為樣本。
        2. **頻段修復：** 使用 Spectral Frequency Display (頻譜圖) 找出突兀的冷氣頻率或電流聲，使用 Notch Filter 精準切除。
        3. **動態處理：** 加入 Noise Gate (噪音門)，將 Threshold 設定在背景音量之上、人聲之下，讓無講話時段自動靜音。
        4. **注意：** 降噪切勿過度，寧可保留微小底噪，也要確保人聲自然，避免產生「機器人音」。
        """
    )
    
with st.expander("Podcast 節目企劃心法（金聲獎經驗談）"):
    st.markdown(
        """
        * **黃金前 3 分鐘：** 現代人耐心有限，節目開頭必須直接拋出本集最吸引人的「鉤子 (Hook)」，或剪輯一段最精彩的精華對話作為冷開場 (Cold Open)。
        * **聲音的視覺化：** 單純講話容易疲勞，善用過場音樂 (Bumper Music) 和環境音效來暗示場景轉換，幫助聽眾在腦海中建構畫面。
        """
    )