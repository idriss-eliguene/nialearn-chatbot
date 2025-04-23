import streamlit as st

def nia_response(message):
    if "devops" in message.lower():
        return "Le DevOps, c’est un métier où tu automatises les déploiements. Tu veux apprendre ? Commence avec Linux + Git + Docker."
    elif "je veux apprendre" in message.lower():
        return "Dis-moi ce que tu veux apprendre et combien de temps tu as. Je te propose un mini-plan."
    else:
        return "Je suis Nia, ton mentor tech. Pose-moi des questions sur la programmation, le cloud, ou les métiers du numérique."

st.title("💬 NiaLearn - Coach IA pour jeunes techs")
user_input = st.text_input("Toi :", placeholder="Je veux apprendre le cloud...")
if st.button("Parler à Nia"):
    if user_input:
        response = nia_response(user_input)
        st.markdown(f"**Nia 🧠:** {response}")
