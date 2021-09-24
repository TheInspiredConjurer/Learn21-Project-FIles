class Shape {
  constructor(name, sides, sideLength) {
    this.name = name;
    this.sides = sides;
    this.sideLength = sideLength;
  }

  calcPerimeter(name, sides, sideLength) {
    let perimeter = (sides * sideLength);
    console.log("The perimeter of " + name + " of side " + sides + " and having dimensions of " + sideLength + " is: " + perimeter);
  }

  calcPerimeter(name, length, breadth,) {
    let perimeter = 2 * (length * breadth);
    console.log("The perimeter of " + name + " of length " + length + " and breadth " + breadth + " is: " + perimeter);
  }
}

let Square = new Shape();
Square.calcPerimeter("Square", 4, 4);
let Rectangle = new Shape();
Rectangle.calcPerimeter("Rectangle", 2, 3);
