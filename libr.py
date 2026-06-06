from pyclay import *
import pyclay._renderer as renderer
import pyclay._server as server



page("Home")

image(src="assets/5499_Photo.jpeg", width="200px",height="200px")
navbar(
    title="Sailatha Shetty Portfolio",
    links=[
        {"text": "Home", "href": "#Home"},
        {"text": "Projects", "href": "#Projects"},
        {"text": "Industry Experiences", "href": "#IndustryExperiences"},
        {"text": "Contact Details", "href": "#About"}
    ],
    
    variant="simple"
)

heading("About Me", level=1)
text("I am Sailatha Shetty, B.Tech 2026 graduate from Ramrao Adik Institute of Technology. I hold a degree in Computer Engineering with minor in Data Science. I am looking forward to actively collaborate with industry experts and solving real world problems using the skillset I have aquired throughout my B.Tech journey.")

card(
    title="Techstacks",
    body=""" SAP S/4 Hana Sourcing and Procurement, React, Spring Boot, Express.js , FastAPI , PostgreSQL, MySQL, MongoDB, Firebase, Tailwind CSS, MERN Stack, AI/ML Stack, Java Enterprise Stack
"""
)
heading("Copyrights filed", level=2)

blockquote(
    "Registered Software copyright for the project GlamIT: a social fashion webapp"
)
heading("Hackathons", level=2)

blockquote(
    """HACKCELESTIAL National Level Hackathon Finalist: Developed and presented HealthLine- an innovative concept of an AI-powered healthcare portal designed to seamlessly connect
hospitals and patients through an agentic AI interface."""
)
heading("Certifications", level=2)

blockquote(
    "freeCodeCamp: JavaScript algorithms and data structures, Udemy: SAP S/4 HANA Sourcing and Procurement, CISCO: Introduction to CyberSecurity, Alteryx: Machine Learning Fundamentals,Designer Core Certified,Alteryx Foundation, AWS: AWS Academy Graduate-Cloud Architecting"
)



# =========================
# DASHBOARD PAGE
# =========================

page("Projects")

heading("Projects", level=1)

text("Overview of projects")

card(
    title="Artsy-Social| Mongo DB, React js, Express js, Node js, Python",
    body="""Developed a MERN + AI/ML stack eCommerce web app exclusively for artists, implementing JWT authentication, profile management,
product uploads, cart, orders, and secure payment integration. Integrated a real-time hybrid recommendation engine (content-based + collaborative filtering) with FastAPI, MongoDB, and
scikit-learn, enabling continuous learning from streaming user order data to produce dynamic top-5 product recommendations;
achieved high accuracy with 1 of 5 items purchased (leave-one-out validated)."""
)

card(
    title="Satya Sethu- Bridge to the Truth| Python, Flask, React-Native, Hugging Face Transformers (RoBERTa), PyTorch, NLTK, Tesseract OCR, Pillow, BeautifulSoup, Newspaper3k, Cloudinary, SerpAPI, NewsAPI, and GNews API",
    body="""Developed a fake news detection webapp with an accuracy of 91%. The webapp handles multimedia inputs like texts, images,
    news urls, ocr scanning and predicts if the news is fake using Natural Language Processing as well as verification with news APIS and reverse image searching.
    It also displays and updates the real time verified news for the users."""
)

card(
    title="Sach-AI | Python, React, Tailwind CSS, Flask, Twitter APIv2",
    body="""Developed a fake Twitter account detection web app. Fetched real-time Twitter data using Twitter APIv2. Used three models—Random Forest, KNN, and Linear SVC—to classify Twitter accounts with 83% accuracy. Supports a browser extension where users can report fake accounts in real time. AI assistant flags potential red flags."""
)

card(
    title="GlamIt | React-Native, Tailwind CSS, Firebase, Chakra UI",
    body="""Created a social fashion app for users to share and engage with fashion content. Enabled features like account creation, post sharing, glamBoard viewing, liking, and commenting."""
)

card(
    title="Echo Memory | React, Node.js, Firebase",
    body=""" Built a photo diary and audio-book web app for individuals with early-stage dementia. Upload photographs,date of the event and people included, upload audio memories of loved ones and about dementia section"""
)

card(
    title="Whatsapp Bot | Selenium web driver automation",
    body=""" Built a whatsapp bot to automate cold texting clients through whatsapp web using selenium web driver"""
)

# =========================
# Industry Experiences
# =========================

page("IndustryExperiences")

heading("EY GDS Internship")

card(
    title="4 months Hybrid internship",
    body=""" Gained industry relevant knowledge and hands on experience with SAP S/4 HANA Sourcing and Procurement module.
    Trained on P2P (Procure-to-Pay cycle) execution, MRP (Material Requirement Planning), Material Master, Vendor Master, Pricing Procedure.
    Delivered an evaluatory mini project on Advanced P2P cycle execution with automatic freight calculation, tolerance check and 3-way innvoice matching.
"""
)


# =========================
# ABOUT PAGE
# =========================

page("About")

heading("Academic and Contact Details", level=1)


card(
    title="Email-ID",
    body=""" shettysailatha@gmail.com
"""
)

card(
    title="GITHUB",
    body=""" github.com/SAILATHA-284
"""
)

card(
    title="LinkedIn",
    body=""" linkedin.com/in/Sailatha-Shetty
"""
)
card(
    title="Leetcode",
    body="""saishe
"""
)
card(
    title="Academic scores",
    body="""B-TECH Computer Engineering minor in Data Science: 9.6 cgpa,
    12th Grade, Percentage: 87.5%,
    10th Grade, Percentage: 97%
"""
)





footer("© 2026 Sailatha Shetty")

# =========================
# RENDER + SERVE
# =========================

html = renderer.render_page("Home")

server.serve(html)

input()
