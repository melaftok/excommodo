def convert_to_int(qty, decimal):
  """Converts a quantity with a decimal to an integer.

  Args:
    qty: The quantity to convert.
    decimal: The number of decimal places in the quantity.

  Returns:
    The integer representation of the quantity.
  """

  return int(qty * int("".join(["1"] + ["0"] * decimal)))
