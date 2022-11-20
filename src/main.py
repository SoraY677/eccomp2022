import resolver

def run():
  resolver.first_generate()

  for i in range(len(1000)):
    resolver.process_generate()
    resolver.cross()
    resolver.select()
    resolver.mutate()
    resolver.union()
    pass
