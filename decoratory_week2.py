import functools



# @decorator
#  def decorated():
#    print('Hello')

#  decorated = decorator(decorated)

#  print(decorated())
#  print(decorated.__name__)


#  def logger(func):
#    @functools.wraps(func)
#    def wrapped(*args, **kwargs):
#        result = func(*args, **kwargs)
#        with open('log.txt', 'w') as f:
#            f.write(str(result))
#            return result
#    return wrapped

#  @logger
#  def summator(num_list):
#      return sum(num_list)

#  print(summator([1, 2, 3, 4, 5]))
#  print(summator.__name__)
#  with open('log.txt', 'r') as f:
#    print('log.txt: {}'.format(f.read()))


#  def logger_(filename):
#    def decorator(func):
#        def wrapped(*args, **kwargs):
#            result = func(*args, **kwargs)
#            with open(filename, 'w') as f:
#                f.write(str(result))
#            return result
#        return wrapped
#    return decorator


#  @logger_('new_log.txt')
#  def summator_(num_list):
#    return sum(num_list)

#  summator_([1, 2, 3, 4, 5, 6, 7])

#  with open('new_log.txt', 'r') as f:
#    print('new_log.txt: {}'.format(f.read()))


#  def first_decorator(func):
#    def wrapped():
#        print('Inside first_decorator product')
#        return func()
#    return wrapped

#  def second_decorator(func):
#    def wrapped():
#        print('Inside second_decorator product')
#        return func()
#    return wrapped

#  @first_decorator
# @second_decorator
# def decorated():
#    print('Finally called ...')

#  decorated = first_decorator(second_decorator)

def bold(func):
    def wrapped():
        return "<b>" + func() + "<b>"
    return wrapped

def italic(func):
    def wrapped():
        return "<i>" + func() + "<i>"
    return wrapped


@bold
@italic
def hello():
    return "hello world"

print(hello())