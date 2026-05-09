from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
    ValidationError
)

print("\n===== VALIDATION TESTS =====")

try:
    print(validate_symbol("btcusdt"))
    print(validate_side("buy"))
    print(validate_order_type("market"))
    print(validate_quantity("0.001"))
    print(validate_price(None, "MARKET"))

    print("\nAll validations passed successfully!")

except ValidationError as error:
    print(f"Validation Failed: {error}")