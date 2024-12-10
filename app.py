from flask import Flask, render_template, request, redirect, url_for
from linkedlist import LinkedList

app = Flask(__name__)

# Initialize the linked list
linked_list = LinkedList()

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

@app.route('/works/stack')
def works_stack():
    return render_template('stack.html')

@app.route('/works/queue')
def works_queue():
    return render_template('queue.html')

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
