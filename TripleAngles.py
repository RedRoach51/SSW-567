import pytest;

class NonexistantTriangle(Exception):
    pass;

def classify_triangle(a,b,c):
    string = "";
    Equil_check = False;
#   if a <= 0 or b <= 0 or c <= 0:
#       raise NonexistantTriangle("No Triangle exists with the sides {}{}{}.".format(a,b,c));
    if a == b and b == c:
        string += "Equilateral";
        Equil_check = True;
    if (a == b or b == c or c == a) and not Equil_check:
        string += "Isoceles";
        Equil_check = True;
    if not Equil_check:
        string += "Scalene";
    a2 = a^2; b2 = b^2; c2 = c^2;
    if (a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2):
        string += " Right"
    return string;

def test_scalene():
    assert classify_triangle(2,1,3) == "Scalene";
    assert classify_triangle(3,4,5) == "Scalene Right";
    assert classify_triangle(5,4,3) == "Scalene Right";

def test_isoceles():
    assert classify_triangle(1,1,3) == "Isoceles";
    assert classify_triangle(1,3,1) == "Isoceles";
    assert classify_triangle(3,1,1) == "Isoceles";

def test_equilateral():
    assert classify_triangle(1,1,1) == "Equilateral";

def test_inputs():
    with pytest.raises(TypeError):
        assert classify_triangle(1.0,2.0,3.0);
    with pytest.raises(TypeError):
        assert classify_triangle("One", "Two", "Three");
    with pytest.raises(NonexistantTriangle):
        assert classify_triangle(-1,-1,-1);
    with pytest.raises(NonexistantTriangle):
        assert classify_triangle(0,0,0);

print(classify_triangle(int(input()),int(input()),int(input())));
