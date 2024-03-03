from openai import OpenAI
import os 
import json
import time
#%env OPENAI_API_KEY=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
client = OpenAI(api_key=os.environ.get("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"))


##### -------------------------------------function-----------------------------------
def show_json(obj):
    display(json.loads(obj.model_dump_json()))
def submit_message(assistant_id, thread, user_message):
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=user_message
    )
    # return client.beta.threads.runs.create(
    #     thread_id=thread.id,
    #     assistant_id=assistant_id,
    #)
def run_thread(assistant_id,thread_id ):
    
    return client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )
def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(2)
    return run
def pretty_print(thread_message):
    print("# Messages")
    print(f"{thread_message[-1].role}: {thread_message[-1].content[0].text.value}")
    print()
def create_thread_and_run(user_input):
    thread = client.beta.threads.create()
    run = submit_message(assistant.id, thread, user_input)
    return thread, run

def get_response(thread):

    thread_message= client.beta.threads.messages.list(thread_id=thread.id, order="asc")

    return  thread_message



##### -------------------------------------------------------------------------------

assistant = client.beta.assistants.create(
    name="CLA",
    instructions="""
Sink into the role of a supportive and informed college tutor for brief Q&A interactions.
Aid a student with quick assignment-related pointers and concise advice. Offer clear explanations and constructive feedback in a few sentences.
Show your patience, adaptability, and effective communication skills to create a positive and resourceful tutoring experience.
Respond briefly to the student's immediate queries or doubts and promote a setting that inspires learning and independent problem-solving.
Tailor your short responses to the specific subject matter or assignment details for helpful, targeted assistance.
Make sure your responses are short, consise and fit in a text message. 

""",
    model="gpt-3.5-turbo",    
)




# def get_response(thread):

#     thread_message= client.beta.threads.messages.list(thread_id=thread.id, order="asc")

#     return  thread_message.data

thread1 = client.beta.threads.create()

while True :
    
    thread = client.beta.threads.create()
    m = input('User :')
    submit_message(assistant.id, thread1, m)
    pretty_print(get_response(thread1))
    run = run_thread(assistant.id, thread1)
    run = wait_on_run(run, thread1)
    pretty_print(get_response(thread1))



   
    
