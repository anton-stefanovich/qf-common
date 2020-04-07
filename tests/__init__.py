
def variants(*args, **kwargs) -> tuple:
    if args:  # unnamed values will be provided as 'variant'
        kwargs.update(dict(variant=args))

    variants_values = list(kwargs.values())
    return ','.join(kwargs.keys()), variants_values \
        if len(variants_values) > 1 else variants_values[0]


def parametrize(*args, **kwargs):
    from pytest import mark
    return mark.parametrize(
        *variants(*args, **kwargs))
