from flask import Flask, render_template, request, redirect, url_for
from linkedlist import LinkedList
from stack import Stack, ShuntingYard
from queue import QueueLinkedList, DequeLinkedList

app = Flask(__name__)

# Initialize the linked list
linked_list = LinkedList()

# Initialize the stack
stack = Stack()

# Initialize the queue
queue = QueueLinkedList()

def get_queue_elements():
    elements = queue.display()
    return [node['data'] for node in elements]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

# Redirect routes for the 8 profiles
@app.route('/profile1')
def profile1():
    return render_template('profile1.html')

@app.route('/profile2')
def profile2():
    return render_template('profile2.html')

@app.route('/profile3')
def profile3():
    return render_template('profile3.html')

@app.route('/profile4')
def profile4():
    return render_template('profile4.html')

@app.route('/profile5')
def profile5():
    return render_template('profile5.html')

@app.route('/profile6')
def profile6():
    return render_template('profile6.html')

@app.route('/profile7')
def profile7():
    return render_template('profile7.html')

@app.route('/profile8')
def profile8():
    return render_template('profile8.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/works/linkedlist', methods=['GET', 'POST'])
def works_linkedlist():
    message = None
    linked_list_elements = linked_list.print_list()
    if request.method == 'POST':
        action = request.form.get('action')
        data = request.form.get('data', '')

        if action == 'insert_beginning':
            linked_list.insert_at_beginning(data)
            message = f"Inserted '{data}' at the beginning."
        elif action == 'insert_end':
            linked_list.insert_at_end(data)
            message = f"Inserted '{data}' at the end."
        elif action == 'search':
            found = linked_list.search(data)
            message = f"'{data}' is {'found' if found else 'not found'} in the list."
        elif action == 'remove_beginning':
            message = linked_list.remove_at_beginning() or "Removed the first element."
        elif action == 'remove_end':
            message = linked_list.remove_at_end() or "Removed the last element."
        elif action == 'remove_at':
            message = linked_list.remove_at(data)

        linked_list_elements = linked_list.print_list()

    return render_template('linkedlist.html', message=message, elements=linked_list_elements)

@app.route('/works/stack', methods=['GET', 'POST'])
def works_stack():
    message = None
    stack_elements = []

    if request.method == 'POST':
        action = request.form.get('action')
        data = request.form.get('data', '')

        if action == 'push':
            stack.push(data)
            message = f"Pushed '{data}' onto the stack."
        elif action == 'pop':
            popped = stack.pop()
            message = f"Popped '{popped}' from the stack." if popped else "The stack is empty."
        elif action == 'peek':
            top = stack.peek()
            message = f"Top of the stack is '{top}'." if top else "The stack is empty."

    # Get the current stack elements
    current = stack.top
    while current:
        stack_elements.append(current.data)
        current = current.next

    return render_template('stack.html', message=message, elements=stack_elements)

@app.route('/works/stack/infix_to_postfix', methods=['GET', 'POST'])
def infix_to_postfix():
    message = None
    postfix_steps = []

    if request.method == 'POST':
        infix_expression = request.form.get('infix_expression', '').strip()
        if infix_expression:
            try:
                shunting_yard = ShuntingYard()
                postfix_steps = shunting_yard.infix_to_postfix(infix_expression)
                message = "Conversion completed successfully."
            except Exception as e:
                message = f"Error: {e}"
        else:
            message = "Please provide a valid infix expression."

    return render_template('stack_infix_to_postfix.html', message=message, steps=postfix_steps)

@app.route('/works/queue', methods=['GET', 'POST'])
def works_queue():
    message = None
    queue_elements = get_queue_elements()

    if request.method == 'POST':
        action = request.form.get('action')
        data = request.form.get('data', '')

        if action == 'enqueue':
            queue.enqueue(data)
            message = f"Enqueued '{data}'."
        elif action == 'dequeue':
            dequeued = queue.dequeue()
            message = f"Dequeued '{dequeued}'." if dequeued else "The queue is empty."

        queue_elements = get_queue_elements()

    return render_template('queue.html', message=message, elements=queue_elements)

@app.route('/works/binarytree')
def works_binarytree():
    return render_template('binarytree.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)