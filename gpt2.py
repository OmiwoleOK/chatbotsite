import streamlit as st
from streamlit_option_menu import option_menu




#vertical menu
def main():
    
    with st.sidebar:
            navigation = option_menu (
            menu_title= None, 
            options=["FLOWAPEX", "OUR SERVICES", "CORE VALUE", "CHAT WITH US"],
            icons=["tsunami","reception-4", "suit-club", "chat-text"],
            menu_icon="cast",
            default_index=0,
            )
        

    # Sidebar navigation links
    #st.sidebar.title("Varieties")
    #navigation = st.sidebar.radio("Go to", ["Home", "Customer Service Chatbot", "Onboarding Chatbot", "Staff Training Chatbot", "Prospecting Chatbot"])

    # Main content section based on navigation selection
            if navigation == "FLOWAPEX":
                 st.write('''We are Chatbots Developer. Our chatbots are designed to be seamlessly deployed across multiple platforms, including websites, mobile apps, social media, 
                      and messaging platforms. This ensures your customers can engage with your chatbot wherever they prefer''')
            elif navigation == "OUR SERVICES":
                st.write('''Ours services involve deployment of Customer Service Chatbot, Prospecting Chatbot, Onboarding Chatbot and Staff training Chatbot on different channels''')
            elif navigation == "CORE VALUE":
                st.write('''Our Core Values are Empathy, Integrity and Rescilience''')
            elif navigation ==  "CHAT WITH US":
                st.write('''Chat with us and submit your enquiry. Note that whatsapp chat is " +2348038585391''')
            elif navigation ==  "Prospecting Chatbot":
                prospecting_page()

def home_page():
    st.header("Welcome FLOWAPEX AI Automation!")
    st.subheader("Your One-Stop Solution for Chatbot Development")

    # Create two columns with a ratio of 2:1
    col1, col2 = st.columns([3, 2])
   
    # Replace 'path/to/your/chatty.mp4' with the actual file path of your MP4 video
    with col2:
        video_path = 'assets/chatty.mp4'
        st.video(video_path)
        st.image('assets/AIchatbot2b.jpg', caption='Chatbot', use_column_width=True)
        st.image('assets/AIchatbot1.jpg', caption='Chatbott', use_column_width=True)



    with col1:
        st.write('''Welcome to FLOWAPEX AI Automation Agency - Your Chatbot Development Partner 
             , we specialize in creating innovative and powerful chatbot solutions that redefine customer interactions and drive business 
             growth. With our expertise in chatbot development, we offer you the opportunity 
             to revolutionize your customer engagement strategy and maximize your profits.

 BENEFITS OF OUR CHATBOT SOLUTIONS
             
Seamless Customer Interactions: Our chatbots offer natural and intuitive conversations that make your customers feel heard and understood, enhancing their overall experience.

24/7 Availability: Never miss a customer inquiry again. Our chatbots are available round the clock, ensuring instant responses and improved customer satisfaction.

Efficient Problem Solving: Empower your customers with quick solutions. Our chatbots can address common queries and guide users through troubleshooting steps, reducing support load on your team.

Personalized Recommendations: Deliver personalized product recommendations and tailored experiences to each user, boosting cross-selling and upselling opportunities.

Data-Driven Insights: Gain valuable insights into customer behavior and preferences through chatbot interactions, enabling data-driven decisions for targeted marketing campaigns.''')
        st.subheader("WhatsApp Chat : +2348038585391")
def services_page():

    st.header("Customer Services Automation")
    st.write("Our Customer Service Automation Chatbot provides the folowing benefits.")
    col1, col2 = st.columns([3, 2])

    with col1:
        
        st.write('''1. Seamless Customer Interactions:
             Our chatbots offer natural and intuitive conversations that make your customers
               feel heard and understood, enhancing their overall experience.''')
    
        st.write('''2. 24/7 Availability:
             Never miss a customer inquiry again. Our chatbots are available round the clock,
             ensuring instant responses and improved customer satisfaction.''')
    
        st.write('''3. Efficient Problem Solving:
             Empower your customers with quick solutions. Our chatbots can address common 
             queries and guide users through troubleshooting steps, reducing support load on your team.''')

        st.write('''4. Personalized Recommendations:
              Deliver personalized product recommendations and tailored experiences to each user, boosting 
             cross-selling and upselling opportunities.''')
        
        st.subheader("WhatsApp Chat : +2348038585391")
    with col2:
        video_path = 'assets/animation_lktozk16.mp4'
        st.video(video_path)
        st.image('assets/AIchatbot2b.jpg', caption='Chatbot', use_column_width=True)
        st.image('assets/AIchatbot1.jpg', caption='Chatbott', use_column_width=True)

def about_us_page():
    st.header("Onboarding Chatbot")

    st.write( '''Onboarding chatbots offer a range of benefits that contribute to a smoother and more
              efficient onboarding process for both employees and customers. Here are some key advantages:''')
    col1, col2 = st.columns([3, 2])
   
    # Replace 'path/to/your/chatty.mp4' with the actual file path of your MP4 video
    with col2:
        video_path = 'assets/animation_lktnuchx.mp4'
        st.video(video_path)
        st.image('assets/AIchatbot2b.jpg', caption='Chatbot', use_column_width=True)
        st.image('assets/AIchatbot1.jpg', caption='Chatbott', use_column_width=True)
    with col1:
        st.write('''
        24/7 Availability: Onboarding chatbots are available around the clock, allowing new hires and users to access 
        information and assistance whenever they need it, regardless of time zones or working hours.         

        Instant Responses: Chatbots provide instant responses to common questions and inquiries, reducing the waiting 
        time for information and guidance during the onboarding process.
                 
        Consistent Information: Onboarding chatbots ensure that all users receive consistent and accurate information. 
        This reduces the risk of miscommunication and ensures that everyone is on the same page.
        
        Cost-Efficiency: Automating routine onboarding tasks with chatbots reduces the need for human intervention 
        in basic inquiries, freeing up HR and support staff to focus on more complex issues.
                 
        Real-time Feedback: Chatbots can collect feedback from new hires and users during the onboarding process,
        helping organizations identify areas for improvement and enhance the onboarding experience.
                 
        
        ''')
        st.subheader("WhatsApp Chat : +2348038585391")

def contact_page():
    st.header("Staff Training Chatbot")

    st.write( '''Staff training chatbots provide employees with access to training materials and resources around the clock. Employees can 
             learn at their own pace, making training more flexible and accommodating different schedules.''')
    col1, col2 = st.columns([3, 2])
   
    # Replace 'path/to/your/chatty.mp4' with the actual file path of your MP4 video
    with col2:
        video_path = 'assets/animation_lktochir.mp4'
        st.video(video_path)
        st.image('assets/AIchatbot2b.jpg', caption='Chatbot', use_column_width=True)
        st.image('assets/AIchatbot1.jpg', caption='Chatbott', use_column_width=True)

    with col1:
        st.write('''
        24/7 Availability: Onboarding chatbots are available around the clock, allowing new hires and users to access 
        information and assistance whenever they need it, regardless of time zones or working hours.         

        Consistent and Standardized Training: A chatbot delivers the same training content to all employees, ensuring consistency in the information 
        provided. This helps establish standardized knowledge levels across the organization.
        
        Interactive Learning Experience: Staff training chatbots engage employees through interactive quizzes, simulations, and multimedia content, making the learning
        process more engaging and effective. This interactive approach enhances knowledge retention.
        
        Personalized Learning Paths: Chatbots can tailor training based on individual employee roles, experience levels, and learning preferences. This personalized
        approach ensures that each employee receives the most relevant and effective training.
                 
        Real-time Feedback and Assessment: Chatbots provide immediate feedback on quizzes and assessments, enabling employees to gauge their progress and identify areas for improvement. 
        This instant feedback loop enhances the learning process and encourages continuous improvement.
        ''')
        
        st.subheader("WhatsApp Chat : +2348038585391")

def prospecting_page():
    st.header("Prospecting Chatbot")

    st.write( '''A prospecting chatbot can engage website visitors and social media users, capturing their contact information and qualifying 
             them as potential leads. This automated lead generation process expands your customer base..''')
    col1, col2 = st.columns([3, 2])
   
    # Replace 'path/to/your/chatty.mp4' with the actual file path of your MP4 video
    with col2:
        video_path = 'assets/animation_lktnxvgq.mp4'
        st.video(video_path)
        st.image('assets/AIchatbot2b.jpg', caption='Chatbot', use_column_width=True)
        st.image('assets/AIchatbot1.jpg', caption='Chatbott', use_column_width=True)

    with col1:
        st.write('''
       Instant Customer Engagement: Chatbots can initiate conversations with prospects as soon as they land on your website or interact with your marketing campaigns. 
       This immediate engagement captures prospects' attention and increases the chances of conversion.
        
        Data Collection and Insights: Prospect chatbots can gather valuable data about prospects' preferences, pain points, and needs. This information helps your 
        sales team tailor their approach, leading to more targeted and effective sales interactions.
        
                 
        Lead Nurturing and Follow-up: Chatbots can nurture leads by sending personalized follow-up messages, educational content, and product information. 
        This continuous engagement keeps prospects engaged and informed throughout the buying journey.
        
        Schedule Appointments and Demos: Prospect chatbots can schedule appointments, product demos, and consultations with sales representatives. This 
        streamlined process ensures that prospects receive prompt and convenient access to your team..
        ''')

        st.subheader("WhatsApp Chat : +2348038585391")

selected = option_menu (
            menu_title= None, 
            options=["Home", "Customer", "Onboarding", "Prospecting"],
            icons=["house-heart","chat-square-fill", "chat-square-heart", "chat-text", "chat-heart"],
            #menu_icon="cast",
            #default_index=0,
            orientation="horizontal",
            )
            
if selected == "Home":
            home_page()
elif selected == "Customer":
            services_page()
elif selected == "Onboarding":
            about_us_page()
elif selected ==  "Staff":
            contact_page()
elif selected ==  "Prospecting":
            prospecting_page()


if __name__ == "__main__":
        main()
