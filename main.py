import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="Dhananjay | Portfolio", layout="wide")
header_html = """
<div id="app-header">
  <canvas id="canvas"></canvas>
</div>

<style>
#app-header {
  position: relative;
  width: 100%;
  height: 250px;
  overflow: hidden;
  background: #000;
}

#canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>

<script type="module">
import TubesCursor from "https://cdn.jsdelivr.net/npm/threejs-components@0.0.19/build/cursors/tubes1.min.js"

const canvas = document.getElementById('canvas');

function resizeCanvas() {
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
}

resizeCanvas();
window.addEventListener('resize', resizeCanvas);

const app = TubesCursor(canvas, {
    tubes: {
        colors: ["#f967fb", "#53bc28", "#6958d5"],
        lights: {
            intensity: 100, // reduce intensity to avoid overflow glow
            colors: ["#83f36e", "#fe8a2e", "#ff008a", "#60aed5"]
        },
        scale: 0.45 
    }
});

document.getElementById('app-header').addEventListener('click', () => {
    const colors = randomColors(3)
    const lightsColors = randomColors(4)
    app.tubes.setColors(colors)
    app.tubes.setLightsColors(lightsColors)
})

function randomColors(count) {
    return new Array(count)
        .fill(0)
        .map(() => "#" + Math.floor(Math.random() * 16777215).toString(16).padStart(6, '0'))
}
</script>
"""

components.html(header_html, height=250, scrolling=False)


tab1, tab2, tab3, tab4 = st.tabs(["HOME", "ABOUT ME", "PROJECTS", "CONTACT ME"])
with tab1:
    st.image("assets/Welcome.gif", use_container_width=False)
    st.title("Hi, I'm Dhananjay 👋")
    st.write("""
    Welcome to my portfolio website!  
    The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.
    """)
    st.image("assets/Snakeladder.gif", use_container_width=False, width=400)

# elif page == "🙋‍♂️ About Me":
with tab2:
    st.header("About Me")
    st.write("""
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam nec augue ac erat egestas porta. Sed ac metus quis mauris vehicula elementum at in est. Suspendisse quis orci vitae enim consequat consectetur. Curabitur elit nulla, iaculis gravida purus ut, euismod tristique ligula. Integer at orci non felis elementum malesuada sed vel urna. Duis pulvinar turpis a magna molestie luctus. Proin in orci diam. Quisque cursus condimentum leo ac facilisis. Proin sodales, neque at ultricies tincidunt, quam dolor consectetur nulla, a dapibus tortor lacus eget mauris. Sed tincidunt felis felis, ac lobortis metus sagittis vel.
    """)

# elif page == "💻 Projects":
with tab3:
    st.header("My Projects")
    
    st.subheader("ABC")
    st.write("""
   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam nec augue ac erat egestas porta. Sed ac metus quis mauris vehicula elementum at in est. Suspendisse quis orci vitae enim consequat consectetur. Curabitur elit nulla, iaculis gravida purus ut, euismod tristique ligula. Integer at orci non felis elementum malesuada sed vel urna. Duis pulvinar turpis a magna molestie luctus. Proin in orci diam. Quisque cursus condimentum leo ac facilisis. Proin sodales, neque at ultricies tincidunt, quam dolor consectetur nulla, a dapibus tortor lacus eget mauris. Sed tincidunt felis felis, ac lobortis metus sagittis vel.
    """)

    st.subheader("DEF")
    st.write("""
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam nec augue ac erat egestas porta. Sed ac metus quis mauris vehicula elementum at in est. Suspendisse quis orci vitae enim consequat consectetur. Curabitur elit nulla, iaculis gravida purus ut, euismod tristique ligula. Integer at orci non felis elementum malesuada sed vel urna. Duis pulvinar turpis a magna molestie luctus. Proin in orci diam. Quisque cursus condimentum leo ac facilisis. Proin sodales, neque at ultricies tincidunt, quam dolor consectetur nulla, a dapibus tortor lacus eget mauris. Sed tincidunt felis felis, ac lobortis metus sagittis vel.
    """)

    st.subheader("GHI")
    st.write("""
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam nec augue ac erat egestas porta. Sed ac metus quis mauris vehicula elementum at in est. Suspendisse quis orci vitae enim consequat consectetur. Curabitur elit nulla, iaculis gravida purus ut, euismod tristique ligula. Integer at orci non felis elementum malesuada sed vel urna. Duis pulvinar turpis a magna molestie luctus. Proin in orci diam. Quisque cursus condimentum leo ac facilisis. Proin sodales, neque at ultricies tincidunt, quam dolor consectetur nulla, a dapibus tortor lacus eget mauris. Sed tincidunt felis felis, ac lobortis metus sagittis vel.
    """)

# elif page == "📞 Contact Me":
with tab4:
    st.header("Contact Me")
    st.write("Feel free to connect or collaborate with me 👇")
    
    st.write("📧 Email: [your.email@example.com](mailto:your.email@example.com)")
    st.write("🌐 LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)")
    st.write("💻 GitHub: [github.com/yourprofile](https://github.com/yourprofile)")
