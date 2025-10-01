# Simple Rule-Based Chatbot
# Student Name: [Your Name]
# Date: October 2025
# Description: A basic chatbot that responds to user greetings and simple questions

def chatbot_response(user_message):
    """
    Function to generate chatbot responses based on user input
    Parameters: user_message (string) - the message from user
    Returns: response (string) - the bot's reply
    """
    
    # Convert message to lowercase for easier comparison
    message = user_message.lower()
    
    # Check for greetings
    if message == "hello" or message == "hi" or message == "hey":
        response = "Hi! Welcome to my chatbot!"
    
    # Check for how are you
    elif message == "how are you" or message == "how are you?":
        response = "I'm fine, thanks! How are you doing?"
    
    # Check for goodbye
    elif message == "bye" or message == "goodbye":
        response = "Goodbye! Have a nice day!"
    
    # Check for name question
    elif message == "what is your name" or message == "what is your name?":
        response = "I am a chatbot created by a student!"
    
    # Check for thank you
    elif message == "thank you" or message == "thanks":
        response = "You're welcome!"
    
    # If message doesn't match any rule
    else:
        response = "Sorry, I don't understand. Try: hello, how are you, or bye"
    
    return response


def main():
    """
    Main function to run the chatbot program
    Uses a loop to keep the conversation going
    """
    
    # Display welcome message
    print("\n" + "="*60)
    print("          WELCOME TO MY SIMPLE CHATBOT")
    print("="*60)
    print("You can chat with me! Type 'bye' to exit.")
    print("-"*60 + "\n")
    
    # Start infinite loop for conversation
    while True:
        # Get input from user
        user_input = input("You: ")
        
        # Check if user wants to exit
        if user_input.lower() == "bye" or user_input.lower() == "goodbye":
            print("Bot:", chatbot_response(user_input))
            print("\nThank you for chatting! Program ending...\n")
            break  # Exit the loop
        
        # Get response from chatbot function
        bot_reply = chatbot_response(user_input)
        
        # Display bot's response
        print("Bot:", bot_reply)
        print()  # Empty line for better readability


# Program starts here
if __name__ == "__main__":
    print("\nStarting Chatbot Program...")
    main()
    print("Program Ended Successfully!")