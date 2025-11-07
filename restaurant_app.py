import streamlit as st

st.set_page_config(page_title="Teddy's Restaurant", page_icon="🍽️")

st.title("🍽️ Create Your Custom Dish")
st.write("Welcome to Teddy’s Food Factory! Select your items below 👇")

# Category
category = st.radio("Choose Category:", ["Veg", "Mushroom", "Non-Veg"])

# Rice Option
rice = st.radio("Rice Option:", ["With Rice", "No Rice"])

# Dish Items
items = st.multiselect(
    "Add 3-4 items:",
    ["Paneer Tikka", "Mushroom Masala", "Chicken Kabab", 
     "Extra Cheese", "Special Sauce", "Fried Onions"]
)

# Dessert
dessert = st.selectbox(
    "Select Dessert 🍰",
    ["Select", "Gulab Jamun", "Chocolate Ice Cream", "Brownie"]
)

# Soup
soup = st.selectbox(
    "Select Soup 🍲",
    ["Select", "Sweet Corn Soup", "Tomato Soup", "Chicken Soup"]
)

# Button
if st.button("✅ Create My Dish"):
    if len(items) < 3:
        st.warning("⚠️ Please choose at least 3 items!")
    elif dessert == "Select" or soup == "Select":
        st.warning("⚠️ Please select dessert & soup!")
    else:
        st.success("🎉 Your Dish is Ready to Serve! 🍽️🔥")
        st.write(f"👨‍🍳 **Category:** {category}")
        st.write(f"🍚 **Rice Option:** {rice}")
        st.write(f"🍢 **Items:** {', '.join(items)}")
        st.write(f"🍰 **Dessert:** {dessert}")
        st.write(f"🍲 **Soup:** {soup}")
        st.balloons()
