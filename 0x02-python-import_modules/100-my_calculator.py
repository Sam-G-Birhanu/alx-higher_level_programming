#!/usr/bin/python3
if __name__ == "__main__":
  from sys import argv
  from calculator_1 import add, sub, mul, div

  def usage():
    print("Usage: {} <a> <operator> <b>".format(argv[0]))
    exit(1)

  def not_found():
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

  def calculate(num1, num2, op):
    try:
      total = {
        "+": add(num1, num2),
        "-": sub(num1, num2),
        "*": mul(num1, num2),
        "/": div(num1, num2),
      }[op]

      print("{:d} {} {:d} = {:d}".format(num1, op, num2, total))
      return total
    except KeyError:
      not_found()

  if len(argv) != 4:
    usage()

  num1 = int(argv[1])
  num2 = int(argv[3])
  op = argv[2]

  calculate(num1, num2, op)
