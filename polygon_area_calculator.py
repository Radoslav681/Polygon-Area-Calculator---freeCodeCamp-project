class Rectangle:
	'''Create a Rectangle class.'''

  def __init__(self, width, height):
    self.height = height
    self.width = width

  def __str__(self):
    if self.height != self.width:
      return f'Rectangle(width={self.width}, height={self.height})'

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    picture = ""
    if self.height > 50 or self.width > 50:
      return 'Too big for picture.'
    for lines in range(self.height):
      picture += f"{'*' * self.width}\n"
    return picture

  def get_amount_inside(self, rectangle):
    h_fit = self.height / rectangle.height
    w_fit = self.width / rectangle.width
    if rectangle.height > self.height or rectangle.width > self.width:
      return 0
    return int(h_fit) * int(w_fit)


class Square(Rectangle):
	'''A Squared class that inherits methods and attributes from the Rectangle class'''

  def __init__(self, side_length):
    self.height = side_length
    self.width = side_length

  def __str__(self):
    if self.height == self.width:
      return f"Square(side={self.height})"

  def set_side(self, side_length):
    self.height = side_length
    self.width = side_length

  def set_width(self, side_length):
    self.set_side(side_length)

  def set_height(self, side_length):
    self.set_side(side_length)
