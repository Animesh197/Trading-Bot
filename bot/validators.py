class ValidationError(Exception):
    """
    Custom exception for validation errors.
    """
    pass


def validate_symbol(symbol: str) -> str:
    """
    Validate trading symbol.
    """

    if not symbol:
        raise ValidationError("Symbol cannot be empty.")

    symbol = symbol.upper()

    if not symbol.endswith("USDT"):
        raise ValidationError(
            "Only USDT trading pairs are supported. Example: BTCUSDT"
        )

    return symbol


def validate_side(side: str) -> str:
    """
    Validate order side.
    """

    if not side:
        raise ValidationError("Side is required.")

    side = side.upper()

    allowed_sides = ["BUY", "SELL"]

    if side not in allowed_sides:
        raise ValidationError(
            f"Invalid side '{side}'. Allowed values: BUY or SELL."
        )

    return side


def validate_order_type(order_type: str) -> str:
    """
    Validate order type.
    """

    if not order_type:
        raise ValidationError("Order type is required.")

    order_type = order_type.upper()

    allowed_types = ["MARKET", "LIMIT"]

    if order_type not in allowed_types:
        raise ValidationError(
            f"Invalid order type '{order_type}'. "
            "Allowed values: MARKET or LIMIT."
        )

    return order_type


def validate_quantity(quantity) -> float:
    """
    Validate order quantity.
    """

    try:
        quantity = float(quantity)

    except ValueError:
        raise ValidationError(
            "Quantity must be a valid number."
        )

    if quantity <= 0:
        raise ValidationError(
            "Quantity must be greater than 0."
        )

    return quantity


def validate_price(price, order_type: str):
    """
    Validate price for LIMIT orders.
    """

    order_type = order_type.upper()

    # MARKET orders don't require prices
    if order_type == "MARKET":
        return None

    # LIMIT orders require price
    if price is None:
        raise ValidationError(
            "Price is required for LIMIT orders."
        )

    try:
        price = float(price)

    except ValueError:
        raise ValidationError(
            "Price must be a valid number."
        )

    if price <= 0:
        raise ValidationError(
            "Price must be greater than 0."
        )

    return price