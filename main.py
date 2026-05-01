from agent import Agent

if __name__=="__main__":
    agent = Agent()
    while True:
        user_input=input("\n你:")
        if user_input.strip().lower() in ['exit','quit']:
            print("结束")
            break

        agent.run(user_input)
