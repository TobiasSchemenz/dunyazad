def run(self):
  subtask(
    self,
    'add_character',
    **{ 'args.role':'protagonist', 'args.name':'Komim', }
  )
  subtask(
    self,
    'add_character',
    **{ 'args.role':'companion', 'args.name':'Anenri', }
  )
  subtask(
    self,
    'add_character',
    **{ 'args.role':'antagonist', 'args.name':'Umyrgai', }
  )
  subtask(
    self,
    'add_character',
    **{ 'args.role':'stranger', 'args.name':'Quollips', }
  )
  yield tn.TaskStatus.Ongoing.InProgress
  spawn_task(self.net, 'setup_provocation')
