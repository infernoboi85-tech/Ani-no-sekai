import streamlit as st

st.set_page_config(page_title="My Anime Hub", layout="wide")
st.title("🎬 My Personal Anime Review Hub")
st.write("Welcome! Here is the collection of my favorite anime series and my personal reviews.")

conn = st.connection("gsheets", type=st.connection.ExperimentalBaseConnection)
sheet_data = conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/1BMXL_DOKLjAuxB6PPKgJmNtOOsbsHV_M_-XoDmQwwCM/edit?usp=sharing")

for index, row in sheet_data.iterrows():
    with st.container(border=True):
        st.subheader(row["title"])
        st.image(row["image"], use_container_width=True)
        st.write(f"📝 **Review:** {row['review']}")
        st.link_button("🎬 Watch Trailer", row["youtube"], use_container_width=True)

with st.sidebar:
    st.markdown("### 📢 AniVerse Channel")
    st.write("Anime အပိုင်းသစ်တွေကို တိုက်ရိုက်ကြည့်ရှုဖို့ ကျွန်တော်တို့ရဲ့ Telegram Channel ထဲကို အခုပဲ ဝင်ရောက်လိုက်ပါဗျာ!")
    st.link_button(
        label="✈️ Join Our Telegram Channel", 
        url="https://t.me/Ani_no_sekai", 
        type="primary",
        use_container_width=True
    )

if "anime_database" not in st.session_state:
    st.session_state.anime_database = [
        {
            "title": "That Time I Got Reincarnated as a Slime",
            "genre": "Isekai / Fantasy",
            "rating": "⭐⭐⭐⭐⭐",
            "image": "https://i.pinimg.com/736x/2b/40/18/2b4018dbb2d656b6fffdc63b0a7c30b4.jpg",
            "review": "A refreshing and highly entertaining Isekai anime. Instead of a typical hero, the protagonist is reincarnated as a humble slime named Rimuru. The show shines with its excellent world-building, kingdom-building aspects, and a vibrant cast of characters. It strikes a perfect balance between lighthearted comedy and epic, high-stakes battles.",
            "trailer": "https://www.youtube.com/watch?v=NORCMu3PHXQ"
        },
        {
        
            "title": "Solo Leveling",
            "genre": "Isekai / Fantasy",
            "rating": "⭐⭐⭐⭐⭐",
            "image": "data:image/webp;base64,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",
            "review": "Pure hype and adrenaline. This anime follows Jinwoo, the weakest hunter, as he gains the unique ability to level up like a video game character. The animation by A-1 Pictures is top-tier, delivering some of the most breathtaking and brutal action sequences in recent years. It’s a thrilling, fast-paced 'zero-to-hero' story.",
            "trailer": "https://www.youtube.com/watch?v=I6JIwjWOhnQ"
        },
        {
            "title": "Re:Zero - Starting Life in Another World",
            "genre": "Isekai / Fantasy",
            "rating": "⭐⭐⭐⭐⭐",
            "image": "https://i.pinimg.com/736x/7d/78/97/7d789796890b598bc075052ea5521316.jpg",
            "review": "A psychological masterpiece disguised as a fantasy Isekai. Subaru Natsuki is summoned to a fantasy world with only one power: \"Return by Death.\" The anime is emotionally intense, dark, and deeply compelling as Subaru suffers repeatedly to save the people he loves. It features incredible character development and complex mysteries.",
            "trailer": "https://www.youtube.com/watch?v=Slz_rahWp6Y"
        },
        {
            "title": "Classroom of the Elite",
            "genre": "Psychological / Thriller",
            "rating": "⭐⭐⭐⭐✨",
            "image": "https://i.pinimg.com/736x/57/ad/b6/57adb66eddc5bd5b3020d60f80d7734c.jpg",
            "review": "A thrilling school-drama driven by intellect and manipulation. At a prestigious high school where students are evaluated strictly by merit, Ayanokoji Kiyotaka pretends to be ordinary but secretly manipulates events from the shadows. The strategic mind games between classes make it highly engaging and addictive.",
            "trailer": "https://www.youtube.com/watch?v=RTvdxGyWV6c"
        },
        {
            "title": "Black Clover",
            "genre": "Action / Shonen",
            "rating": "⭐⭐⭐⭐⭐",
            "image": "https://i.pinimg.com/1200x/4a/57/4c/4a574c73b985f6e8e97001815ebbfdfd.jpg",
            "review": "A classic Shonen anime that starts loud but grows into an absolute masterpiece. Asta, a boy born without magic in a world where magic is everything, aims to become the Wizard King. It features incredible themes of teamwork, epic rivalries, and some of the best hype-filled, multi-character battles in anime history.",
            "trailer": "https://www.youtube.com/watch?v=BwdMT-OiARI"
        },
        {
            "title": "Mashle: Magic and Muscles",
            "genre": "Comedy / Slice of Life",
            "rating": "⭐⭐⭐⭐⭐",
            "image": "https://i.pinimg.com/736x/c2/99/39/c29939310cd3ad2ea7df9766e40d8976.jpg",
            "review": "Think Harry Potter meets One Punch Man. In a world where magic ability determines your social status, Mash Burnedead has zero magic but possesses superhuman physical strength. He decides to smash through magic spells with his bare fists just so he can live peacefully and eat cream puffs. It is absurdly funny and action-packed.",
            "trailer": "https://www.youtube.com/watch?v=hxnl9nYl67k"
        },
        {
            "title": "Wistoria: Wand and Sword",
            "genre": "Action / Shonen",
            "rating": "⭐⭐⭐⭐✨",
            "image": "https://i.pinimg.com/736x/47/e0/aa/47e0aa7aa424142e87863e4da9f3cd33.jpg",
            "review": "A visually spectacular magic-academy anime. Will Serfort wants to fulfill a childhood promise but cannot use magic, so he compensates by mastering the sword. The story might feel familiar, but the jaw-dropping, fluid animation during fight scenes elevates this show into a thrilling spectacle for action lovers.",
            "trailer": "https://www.youtube.com/watch?v=KJclSlaRgCM"
        },
        {
            "title": "Farming Life in Another World",
            "genre": "Comedy / Slice of Life",
            "rating": "⭐⭐⭐⭐⭐",
            "image": "https://i.pinimg.com/736x/c6/ce/60/c6ce6083275d4ad8e979bdb8d743ff2c.jpg",
            "review": "A cozy, wholesome, and incredibly relaxing Isekai. After a painful past life, Hiraku is granted a healthy body and a magical farming tool. He slowly builds a peaceful village filled with diverse fantasy races. It’s the perfect 'slice-of-life' anime to watch when you just want to unwind and feel happy.",
            "trailer": "https://www.youtube.com/watch?v=fvpf3c_87kI"
        },
        {
            "title": "Mushoku Tensei: Jobless Reincarnation",
            "genre": "Isekai / Fantasy",
            "rating": "⭐⭐⭐⭐⭐",
            "image": "https://i.pinimg.com/1200x/9b/31/02/9b31021b2e8a0b9c9c307bfffd5d6165.jpg",
            "review": "Widely considered the grandfather of modern Isekai. It follows Rudeus Greyrat, a former NEET, who gets a second chance at life in a magical world. The anime boasts movie-quality animation, rich world-building, and a deeply flawed protagonist who genuinely grows over time. It handles its fantasy elements with great maturity and realism.",
            "trailer": "https://www.youtube.com/watch?v=M-3YqJA6UlM"
        },
        {
            "title": "Overlord",
            "genre": "Isekai / Fantasy",
            "rating": "⭐⭐⭐⭐✨",
            "image": "https://i.pinimg.com/1200x/3b/c2/56/3bc2566329676a6727b44ece9582d70e.jpg",
            "review": "A fascinating 'villain protagonist' story. Trapped inside a dying MMORPG, Momonga becomes his skeletal avatar, Ainz Ooal Gown, and decides to conquer the world. It’s unique because the main character is overwhelmingly powerful and acts as the 'final boss' of the world. The dark humor and strategic world domination are highly addictive.",
            "trailer": "https://www.youtube.com/watch?v=uhlBqFj9kDw"
        },
        
        {
            "title": "The Eminence in Shadow",
            "genre": "Isekai / Fantasy",
            "rating": "⭐⭐⭐⭐⭐",
            "image": "https://i.pinimg.com/1200x/62/f5/06/62f5062bb78403c76a62da2fae13b85e.jpg",
            "review": "The ultimate chuunibyou (eight-grader syndrome) anime, and it executes it perfectly. Cid Kagenou wants to be the mastermind behind the scenes. He makes up fake conspiracies, but unknowingly, they happen to be 100% real. It is a hilarious, action-packed parody of the Isekai genre that doesn't take itself too seriously.",
            "trailer": "https://www.youtube.com/watch?v=L7LgAbGF-WY"
        },
        {
            "title": "Sword Art Online",
            "genre": "Isekai / Fantasy",
            "rating": "⭐⭐⭐⭐⭐",
            "image": "https://i.pinimg.com/736x/13/9b/ac/139bac6b823788598707a5dabef838f6.jpg",
            "review": "The pioneer that popularized the 'trapped in a video game' genre. Kirito and thousands of players must clear 100 floors of a virtual reality game where dying in-game means dying in real life. While it has its flaws, SAO features iconic music, great romance, and thrilling action that paved the way for modern gaming anime.",
            "trailer": "https://www.youtube.com/watch?v=6ohYYtxfDCg"
        },
        {
            "title": "No Game No Life",
            "genre": "Isekai / Fantasy",
            "rating": "⭐⭐⭐⭐✨",
            "image": "https://i.pinimg.com/736x/82/ee/d8/82eed8198aa6c269bcbf376f7d026a4c.jpg",
            "review": "A vibrant, visually stunning anime where everything—from land ownership to simple arguments—is decided by high-stakes games. Master-strategist siblings Sora and Shiro challenge gods in a world where violence is forbidden. It is incredibly witty, colorful, and packed with brilliant mind games.",
            "trailer": "https://www.youtube.com/watch?v=ETQUp-Omp-A"
        },
        {
            "title": "The Rising of the Shield Hero",
            "genre": "Isekai / Fantasy",
            "rating": "⭐⭐⭐⭐⭐",
            "image": "https://i.pinimg.com/1200x/1a/66/e0/1a66e0e976c754636434e45c645d0f74.jpg",
            "review": "A gripping betrayal-and-redemption story. Naofumi is summoned as the Shield Hero but is immediately framed and hated by the kingdom. Watching him rise from absolute rock bottom through sheer grit and resourcefulness is incredibly satisfying. The first season, in particular, is a phenomenal dark fantasy ride.",
            "trailer": "https://www.youtube.com/watch?v=rKnyi3TRznA"
        },
        {
            "title": "Konosuba: God's Blessing on this Wonderful World!",
            "genre": "Isekai / Fantasy",
            "rating": "⭐⭐⭐⭐⭐",
            "image": "https://i.pinimg.com/1200x/19/b6/69/19b669de60b9877a5b1bf13e6c5ce82c.jpg",
            "review": "The undisputed king of Isekai comedy. Instead of a heroic party, Kazuma is stuck with a useless goddess, a chuunibyou mage who can only cast one explosion spell a day, and a masochistic crusader. The chemistry between the dysfunctional main cast is hilarious, making it a must-watch for laughs.",
            "trailer": "https://www.youtube.com/watch?v=N1AO7k2o78g"
        },
    
        {
            "title": "Kaguya-sama: Love is War",
            "genre": "Romance / Drama",
            "rating": "⭐⭐⭐⭐⭐",
            "image": "https://i.pinimg.com/1200x/98/57/29/9857294ee93f739890176f50981bc176.jpg",
            "review": "The ultimate romantic-comedy. Two elite student council members, Kaguya and Shirogane, are madly in love but too proud to confess first. They treat romance like a war zone, trying to force the other to confess through brilliant, over-the-top psychological schemes. It is incredibly witty, heartwarming, and hilarious.",
            "trailer": "https://www.youtube.com/watch?v=rZ95aZmQu_8"
        },
        {
            "title": "Horimiya",
            "genre": "Romance / Drama",
            "rating": "⭐⭐⭐⭐⭐",
            "image": "https://i.pinimg.com/736x/33/28/e7/3328e71d0cef2ead803c793cbc32c407.jpg",
            "review": "A sweet, refreshing romance that skips the usual frustrating misunderstandings. It follows the popular Hori and the gloomy Miyamura, who discover each other's hidden alter-egos outside of school. The anime is praised for its realistic pacing, lovable side characters, and genuinely wholesome relationship progression.",
            "trailer": "https://www.youtube.com/watch?v=e4RCugyx5No"
        },
        {
            "title": "My Dress-Up Darling",
            "genre": "Romance / Drama",
            "rating": "⭐⭐⭐⭐✨",
            "image": "https://i.pinimg.com/736x/92/43/94/924394830a2633aa7ce0d518e69be0da.jpg",
            "review": "A heartwarming and visually beautiful anime about passions and hobbies. Gojo, a quiet boy who makes traditional dolls, teams up with Marin, a popular and energetic girl who loves cosplay. Their dynamic is incredibly supportive and wholesome, making it one of the best modern rom-coms about creative expression.",
            "trailer": "https://www.youtube.com/watch?v=kgLezQb3jnQ"
        },
        {
            "title": "The Angel Next Door Spoils Me Rotten",
            "genre": "Romance / Drama",
            "rating": "⭐⭐⭐⭐⭐",
            "image": "https://i.pinimg.com/736x/a1/78/4b/a1784b5a475701dd4f46746ae1378481.jpg",
            "review": "The definition of pure wholesomeness and sweetness. A lazy high schooler, Amane, and the school’s 'angel,' Mahiru, live next door to each other and slowly form a bond through cooking and taking care of one another. It is a slow-burn, low-drama romance that will make you smile from ear to ear.",
            "trailer": "https://www.youtube.com/watch?v=-ETeehSB1v4"
        },
        {
            "title": "Toradora!",
            "genre": "Romance / Drama",
            "rating": "⭐⭐⭐⭐✨",
            "image": "https://i.pinimg.com/736x/a7/d7/c8/a7d7c8157364686a815a7207082c8c14.jpg",
            "review": "A classic, emotional Tsundere romance. Ryuji (who looks scary but is gentle) and Taiga (who is tiny but fierce) agree to help each other woo their respective best friends. However, they end up falling for each other instead. It is a beautifully written emotional rollercoaster that balances comedy with deep adolescent drama.",
            "trailer": "https://www.youtube.com/watch?v=ya570uUgQNc"
        },
       
        {
            "title": "Death Note",
            "genre": "Psychological / Thriller",
            "rating": "⭐⭐⭐⭐⭐",
            "image": "https://i.pinimg.com/736x/4d/9a/b2/4d9ab2cd47254df6b035609f64ad3fef.jpg",
            "review": "A legendary psychological thriller that is a staple for every anime fan. Light Yagami finds a notebook that kills anyone whose name is written in it and decides to purge the world of criminals. What follows is a brilliant, high-stakes game of cat-and-mouse between Light and the eccentric detective, L. It is intense, gripping, and timeless.",
            "trailer": "https://www.youtube.com/watch?v=NlJZ-YgAt-c"
        },
        {
            "title": "Monster",
            "genre": "Psychological / Thriller",
            "rating": "⭐⭐⭐⭐⭐",
            "image": "https://i.pinimg.com/736x/97/97/ed/9797ed8bd35332a54283b52dd9a54420.jpg",
            "review": "A slow-burn, realistic psychological masterpiece. Dr. Kenzo Tenma, a brilliant brain surgeon, saves the life of a young boy who grows up to become a charismatic, psychopathic serial killer. Filled with guilt, Tenma hunts him down. It is a deep, dark, and philosophically profound story about morality and human nature.",
            "trailer": "https://www.youtube.com/watch?v=9aS-EgdAq6U"
        },
        {
            "title": "The Promised Neverland (Season 1)",
            "genre": "Psychological / Thriller",
            "rating": "⭐⭐⭐⭐⭐",
            "image": "https://i.pinimg.com/1200x/88/4b/06/884b0684bf0fc7b65901256a1470f872.jpg",
            "review": "A suspenseful horror-thriller that keeps you on the edge of your seat. Orphan children discover a dark, terrifying secret about their peaceful orphanage and must plan a high-stakes escape. The first season is a masterclass in tension, mind games, and emotional storytelling. (Note: Season 1 is highly recommended).",
            "trailer": "https://www.youtube.com/watch?v=ApLudqucq-s"
        },
        {
            "title": "Attack on Titan",
            "genre": "Psychological / Thriller",
            "rating": "⭐⭐⭐⭐⭐",
            "image": "https://i.pinimg.com/1200x/aa/30/53/aa30533276b577b72536642177a73bfa.jpg",
            "review": "A modern masterpiece with an epic scale. Humanity is trapped inside giant walls to protect themselves from man-eating Titans. What starts as a simple survival story evolves into a complex, dark political drama filled with shocking plot twists, moral gray areas, and unforgettable action. The storytelling is flawless from start to finish.",
            "trailer": "https://www.youtube.com/watch?v=LV-nazLVmgo"
        },
        {
            "title": "Erased",
            "genre": "Psychological / Thriller",
            "rating": "⭐⭐⭐⭐✨",
            "image": "https://i.pinimg.com/1200x/da/de/fd/dadefdb4dad6b6a378c63d067e3475ef.jpg",
            "review": "A beautifully written murder-mystery drama. Satoru Fujinuma possesses a power that sends him back in time right before a tragedy occurs. When his mother is murdered, he is sent 18 years into the past to solve a series of childhood kidnappings. It is an emotional, thrilling, and tightly paced mystery.",
            "trailer": "https://www.youtube.com/watch?v=DwmxEAWjTQQ"
        }
    ]

st.sidebar.header("Filter Settings")
genres = ["All Genres", "Isekai / Fantasy", "Action / Shonen", "Psychological / Thriller", "Romance / Drama", "Comedy / Slice of Life"]
selected_genre = st.sidebar.selectbox("Choose a Genre:", genres)

st.sidebar.markdown("---")

# Input Form to Add New Anime from UI
st.sidebar.header("➕ Add New Anime Review")
with st.sidebar.form(key="add_anime_form", clear_on_submit=True):
    new_title = st.text_input("Anime Title:")
    new_genre = st.selectbox("Genre:", genres[1:])
    new_rating = st.select_slider("Rating:", options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    new_image = st.text_input("Image URL or Path:")
    new_review = st.text_area("Your Review:")
    new_trailer = st.text_input("Trailer YouTube URL (Optional):", value="https://www.youtube.com")
    
    submit_button = st.form_submit_button(label="Add to Database")

if submit_button:
    if new_title and new_review and new_image:
        new_anime = {
            "title": new_title,
            "genre": new_genre,
            "rating": new_rating,
            "image": new_image,
            "review": new_review,
            "trailer": new_trailer if new_trailer else "https://www.youtube.com"
        }
        st.session_state.anime_database.append(new_anime)
        st.sidebar.success(f"Successfully added '{new_title}'!")
    else:
        st.sidebar.error("Please fill in Title, Image, and Review sections.")

st.markdown(
    """
    <style>
    .anime-title {
        color: #1E88E5;
        font-family: 'Georgia', serif;
        font-size: 24px;
        font-weight: 600;
    }
    .genre-badge {
        background-color: #E3F2FD;
        color: #0D47A1;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 14px;
        font-weight: bold;
        display: inline-block;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header(f"✨ Styled Anime Gallery ({selected_genre})")

for anime in st.session_state.anime_database:
    if selected_genre == "All Genres" or anime["genre"] == selected_genre:
        with st.container(border=True):
            img_col, detail_col = st.columns([1, 3])
            
            with img_col:
                st.image(anime["image"], use_container_width=True)
                
            with detail_col:
                st.markdown(f"<p class='anime-title'>{anime['title']}</p>", unsafe_allow_html=True)
                st.markdown(f"**Genre:** <span class='genre-badge'>{anime['genre']}</span>", unsafe_allow_html=True)
                st.write(f"**Rating:** {anime['rating']}")
                st.write("**My Review:**")
                st.info(anime["review"])

st.markdown("---")
st.header("🔍 Search Anime Reviews")
search_query = st.text_input("Type Anime Title to Search:", value="")

if search_query:
    st.subheader("Search Results")
    for anime in st.session_state.anime_database:
        if search_query.lower() in anime["title"].lower():
            with st.container(border=True):
                img_col, detail_col = st.columns([1, 3])
                with img_col:
                    st.image(anime["image"], use_container_width=True)
                with detail_col:
                    st.markdown(f"<p class='anime-title'>{anime['title']}</p>", unsafe_allow_html=True)
                    st.markdown(f"**Genre:** <span class='genre-badge'>{anime['genre']}</span>", unsafe_allow_html=True)
                    st.write(f"**Rating:** {anime['rating']}")
                    st.write("**My Review:**")
                    st.info(anime["review"])

st.markdown("---")
st.header("📊 My Anime Hub Analytics")

total_anime = len(st.session_state.anime_database)
five_star_count = sum(1 for anime in st.session_state.anime_database if anime["rating"] == "⭐⭐⭐⭐⭐")

metric_col1, metric_col2 = st.columns(2)
with metric_col1:
    st.metric(label="Total Anime Reviewed", value=total_anime)
with metric_col2:
    st.metric(label="Masterpieces (5★ Anime)", value=five_star_count)

st.markdown("---")
st.header("🎬 Featured Anime Trailers & Music")

# Create a dynamic list of titles directly from database for the dropdown
anime_titles = [anime["title"] for anime in st.session_state.anime_database]
trailer_choice = st.selectbox("Select an Anime to Watch Trailer:", anime_titles)

# Find the selected anime inside database and display its specific trailer link
for anime in st.session_state.anime_database:
    if anime["title"] == trailer_choice:
        st.write(f"### Official Video Presentation: {anime['title']}")
        if "trailer" in anime and anime["trailer"]:
            st.video(anime["trailer"])
        else:
            st.warning("No trailer link provided for this anime yet.")