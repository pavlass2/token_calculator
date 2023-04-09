from token_calculator import calculate_token_amount


# Just for testing
if __name__ == '__main__':
    example_messages = [
        {
            "role": "system",
            "content": "You are a helpful, pattern-following assistant that translates corporate jargon into plain English."
        },
        {
            "role": "user",
            "content": "New synergies will help drive top-line growth."
        },
        {
            "role": "assistant",
            "content": "Things working well together will increase revenue."
        },
        {
            "role": "user",
            "content": "Let's circle back when we have more bandwidth to touch base on opportunities for increased leverage."
        },
        {
            "role": "assistant",
            "content": "Let's talk later when we're less busy about how to do better."
        },
        {
            "role": "user",
            "content": "This late pivot means we don't have time to boil the ocean for the client deliverable."
        }
    ]

    print(calculate_token_amount("gpt-3.5-turbo", example_messages))
