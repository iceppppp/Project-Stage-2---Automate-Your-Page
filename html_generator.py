# Stage 2 - Project_Python


def generate_concept_html(concept_title, concept_description):

# declaration string variable which will receive html content    
    html_content = ""
# to add content to the declared variable    
    html_content +=  '''
<div class="concept">
    <div class="concept-title">
        <h3><u>{concept_title}</u></h3>
    </div>
    <div class="concept-description">
        <p>
            {concept_description}
    </div>
</div>'''
# using strings built in method to replace what's between { }
    return html_content.format(concept_title=concept_title,
                                concept_description=concept_description)

def make_html(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_html(concept_title, concept_description)
# creation of structured data list elements to use when html is being generated.
project_list_of_concepts = [ ['Two is Better Than One', 'This course is a combination of two other Udacity classes'],
                             ['The Web', 'The web is a collection of digital files, hosted on multiple servers.'],
                             ['Tags', 'An HTML tag is always contained within angled brackets.'],
                             ['Some helpful tips:', 'Here are some helpful tips for writing HTML code;'],
                             ['The way websites work', 'Multiple languages constitute the framework of an web page.'],
                             ['Inner structure of a web site', 'Here are some key features of the inner web site structure;'],
                             ['Tree-like structure of HTML', 'Elements in an HTML document are organized into a DOM tree'],
                             ['Related terms:', 'Here are a few more terms related to website structure;'],
                             ['CSS [Cascading Style Sheets]', 'CSS allows programmers to bring style to plain html documents.'],
                             ['Selectors', 'These are the biggest key to understanding CSS.'],
                             ['Including CSS Styling;', 'There several methods to include CSS styling in your web page.'],
                             ['Related terms and helpful tips:', 'Here are some related terms and helpful coding tips.'],
                             ['Code > Test > Refine', 'Finally, here are some tips to help you write your code;'],
                             ['Computer', 'A computer can be programmed to do anything we want.'],
                             ['Program', 'A program tells the computer what to do.'],
                             ['Programming Language', 'Programming language tells a computers what to do.'],
                             ['Python', 'Python is a programming language.'],
                             ['Grammar', 'Human languages and programming languages both have grammar.'],
                             ['Python Expressions', 'A Python <em>"expression"</em> is a legal Python statement.'],
                             ['Debugging', '"<span class="bold">Bugs</span>" are programming mistakes.'],
                             ['Variables in Python', 'Variables are used to create a <em>name</em> which then refers to a <em>value</em>.'],
                             ['Assignment Statement', 'This is a way to introduce a variable, ie Assign value, to a variable.'],
                             ['Equals sign [=] in Python', 'In Python, the equals sign [<span class="code">=</span>] means assignment.'],
                             ['Strings', 'Strings are a sequence of characters surrounded by quotes.'],
                             ['Function', 'A function takes input, does something to that input, and then produces output.'],
                             ['Making vs. Using Functions', 'A function line of code starts with keyword <span class="code">def</span>.'],
                             ['Avoiding Repetition by using Functions', 'Define a function once, and you never have to define it again.'],
                             ['Function without a Return statement?', '<span class="code">return</span> keyword specifies what output the input should produce.'],
                             ['Comparisons', 'Comparisons are the foundation of <span class="code">if</span> statements.'],
                             ['if', 'An <span class="code">if</span> statement is used to make decisions.'],
                             ['else', '<span class="code">else</span> is part of an <span class="code">if</span> statement.'],
                             ['While', 'The <span class="code">while</span> statement is a <em>loop construct</em> in Python.'],
                             ['Structured Data Types', 'Structured data allows you take advantage of that structure.'],
                             ['Mutation', 'Mutation is when the elements of an object are changed in one form or another.'],
                             ['Mutability vs Immutability', '<em>Mutable</em> objects within a list or string can be changed.'],
                             ['Aliasing', 'Aliasing is when there are <em>two</em> different ways to refer to the same object.'],
                             ['List Operations', 'List operations are the mechanisms used to work within the structure of a list.'],
                             ['For Loop', '<em>for loops</em> allow you to iterate over lists.'] ]

# introduction of 'for loop' contruct to iterate through the list elements presented above.
def make_html_for_many_concepts(list_of_concepts):
    html = ""
    for concept in list_of_concepts:
        concept_html = make_html(concept)
        html = html + concept_html
    return html

print make_html_for_many_concepts(project_list_of_concepts)