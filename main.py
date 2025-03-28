import openai
import json
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_social_media_post(prompt, max_tokens=100):
    """
    Generate a social media post using OpenAI's GPT model.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative assistant that writes social media posts that mimic the teenagers that are under influence of the misinformation."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error generating post: {e}")
        return None

def save_post_to_file(post, filename="social_media_posts.json"):
    """
    Save the generated post to a JSON file.
    """
    try:
        data = []
        # Load existing posts if the file exists
        try:
            with open(filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            pass

        # Append the new post
        data.append({"post": post})

        # Save back to the file
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Post saved to {filename}")
    except Exception as e:
        print(f"Error saving post: {e}")

if __name__ == "__main__":
    user_prompt = input("Enter a prompt for the social media post: ")
    generated_post = generate_social_media_post(user_prompt)
    if generated_post:
        print("\nGenerated Post:")
        print(generated_post)
        save_post_to_file(generated_post)