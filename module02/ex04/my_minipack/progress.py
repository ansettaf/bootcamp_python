def progress_bar(iterable, prefix='', size=60):
    total = len(iterable) if hasattr(iterable, '__len__') else None
    for i, item in enumerate(iterable):
        yield item
