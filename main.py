# explaining kung para saan ang code
from pyscript import display, document

def ordering_form(e):
    item1 = document.getElementById('menu1')
    item2 = document.getElementById('menu2')
    item3 = document.getElementById('menu3')
    name = document.getElementById('name1').value
    phone = document.getElementById('phone2').value
    address = document.getElementById('address3').value


    total = (float(item1.value) * item1.checked + 
            float(item2.value) * item2.checked + 
            float(item3.value) * item3.checked)
    
    display(f'Name: {name}', target='output')
    display(f'Address: {address}', target='output')
    display(f'Phone: {phone}', target='output')
    display(f'Total Cost: {total}', target='output')
    



