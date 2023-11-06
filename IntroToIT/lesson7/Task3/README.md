# Generating pictures including Gen algoruthms

## Short documentation 
    - It uses random to generate 3 functions from list of base functions like sin or cos
    and then use it to 3 parametres of pixels(RGB) and then print the first image 64*64
    - after that user choose the best picture and the program improves others and this can go on until user find the best pic

## you need to install libs
    - math
    - operator
    - random
    - parser
    - cv2_rgb
    - numpy 

## creating the funcs
```python
def random_function_string(node, depth):
    if depth == 0:
        if node not in elements:
            return random.choice(elements)
        return node
    elif node in elements:
        return node
    elif node in operations[0]:
        if random.randint(0, 1) == 0 and depth < 4:
            child = random_function_string(random.choice(elements), depth - 1)
            if "cos" in str(node):
                return f"math.cos({child})"
            elif "sin" in str(node):
                return f"math.sin({child})"
            elif "abs" in str(node):
                return f"abs({child})"
            elif "acos" in str(node):
                return f"math.acos({child})"
            elif "asin" in str(node):
                return f"math.asin({child})"
            elif "pow" in str(node):
                return f"math.pow({child}, {random.randint(2, 5)})"
        else:
            child = random_function_string(random.choice(random.choice(operations)), depth - 1)
            if "cos" in str(node):
                return f"math.cos({child})"
            elif "sin" in str(node):
                return f"math.sin({child})"
            elif "abs" in str(node):
                return f"abs({child})"
            elif "acos" in str(node):
                return f"math.acos({child})"
            elif "asin" in str(node):
                return f"math.asin({child})"
            elif "pow" in str(node):
                return f"math.pow({child}, {random.randint(2, 5)})"
    else:
        if random.randint(0, 1) == 0 and depth < 4:
            left_child = random_function_string(random.choice(elements), depth - 1)
        else:
            left_child = random_function_string(random.choice(random.choice(operations)), depth - 1)
        if random.randint(0, 1) == 0 and depth < 4:
            right_child = random_function_string(random.choice(elements), depth - 1)
        else:
            right_child = random_function_string(random.choice(random.choice(operations)), depth - 1)
        if "add" in str(node):
            return f"({left_child} + {right_child})"
        elif "sub" in str(node):
            return f"({left_child} - {right_child})"
        elif "mul" in str(node):
            return f"({left_child} * {right_child})"
```
## Autors
    - Venimu(me)

## No License

## my number 89192707778 (if you want a project you need money)
