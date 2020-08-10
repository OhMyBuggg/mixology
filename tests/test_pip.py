from .helpers import check_solver_result

def test_pip_simple(source):
	source.root_dep("rack", "*")

	source.add("rack-mount", "0.4", deps={})
	source.add("rack-mount", "0.5", deps={})
	source.add("rack-mount", "0.5.1", deps={})
	source.add("rack-mount", "0.5.2", deps={})
	source.add("rack-mount", "0.6", deps={})
	source.add("rack", "0.8", deps={})
	source.add("rack", "0.9", deps={})
	source.add("rack", "0.9.1", deps={})
	source.add("rack", "0.9.2", deps={})
	source.add("rack", "1.0", deps={})
	source.add("rack", "1.1", deps={})
	source.add("activemerchant", "1.2.3", deps={'activesupport': '>= 1.2.3'})
	source.add("activemerchant", "2.2.3", deps={'activesupport': '>= 2.2.3'})
	source.add("activemerchant", "2.3.5", deps={'activesupport': '>= 2.3.5'})
	source.add("actionmailer", "1.2.3", deps={'actionmailer': '= 1.2.3', 'activesupport': '= 1.2.3'})
	source.add("actionmailer", "2.2.3", deps={'actionmailer': '= 2.2.3', 'activesupport': '= 2.2.3'})
	source.add("actionmailer", "2.3.5", deps={'actionmailer': '= 2.3.5', 'activesupport': '= 2.3.5'})
	source.add("actionmailer", "3.0.0-beta", deps={'actionmailer': '= 3.0.0-beta', 'activesupport': '= 3.0.0-beta'})
	source.add("actionmailer", "3.0.0-beta1", deps={'actionmailer': '= 3.0.0-beta1', 'activesupport': '= 3.0.0-beta1'})
	source.add("railties", "1.2.3", deps={'activesupport': '= 1.2.3', 'actionpack': '= 1.2.3', 'actionmailer': '= 1.2.3', 'activerecord': '= 1.2.3'})
	source.add("railties", "2.2.3", deps={'activesupport': '= 2.2.3', 'actionpack': '= 2.2.3', 'actionmailer': '= 2.2.3', 'activerecord': '= 2.2.3'})
	source.add("railties", "2.3.5", deps={'activesupport': '= 2.3.5', 'actionpack': '= 2.3.5', 'actionmailer': '= 2.3.5', 'activerecord': '= 2.3.5'})
	source.add("railties", "3.0.0-beta", deps={})
	source.add("railties", "3.0.0-beta1", deps={})
	source.add("nokogiri", "1.0", deps={})
	source.add("nokogiri", "1.2", deps={})
	source.add("nokogiri", "1.2.1", deps={})
	source.add("nokogiri", "1.2.2", deps={})
	source.add("nokogiri", "1.3", deps={})
	source.add("nokogiri", "1.3.0-1", deps={})
	source.add("nokogiri", "1.3.5", deps={})
	source.add("nokogiri", "1.4.0", deps={})
	source.add("nokogiri", "1.4.2", deps={})
	source.add("weakling", "0.0.1", deps={})
	source.add("weakling", "0.0.2", deps={})
	source.add("weakling", "0.0.3", deps={})
	source.add("activesupport", "1.2.3", deps={})
	source.add("activesupport", "2.2.3", deps={})
	source.add("activesupport", "2.3.5", deps={})
	source.add("activesupport", "3.0.0-beta", deps={})
	source.add("activesupport", "3.0.0-beta1", deps={})
	source.add("actionpack", "1.2.3", deps={'activesupport': '= 1.2.3'})
	source.add("actionpack", "2.2.3", deps={'rack': '~0.9.0', 'activesupport': '= 2.2.3'})
	source.add("actionpack", "2.3.5", deps={'rack': '~1.0.0', 'activesupport': '= 2.3.5'})
	source.add("actionpack", "3.0.0-beta", deps={'rack-mount': '>= 0.5', 'rack': '~1.1', 'activesupport': '= 3.0.0-beta'})
	source.add("actionpack", "3.0.0-beta1", deps={'rack-mount': '>= 0.5', 'rack': '~1.1', 'activesupport': '= 3.0.0-beta1'})
	source.add("activerecord", "1.2.3", deps={'activesupport': '= 1.2.3'})
	source.add("activerecord", "2.2.3", deps={'activesupport': '= 2.2.3'})
	source.add("activerecord", "2.3.5", deps={'activesupport': '= 2.3.5'})
	source.add("activerecord", "3.0.0-beta", deps={'activesupport': '= 3.0.0-beta', 'arel': '>= 0.2'})
	source.add("activerecord", "3.0.0-beta1", deps={'activesupport': '= 3.0.0-beta1', 'arel': '>= 0.2'})
	source.add("rails", "3.0.0-beta", deps={'activesupport': '= 3.0.0-beta', 'actionpack': '= 3.0.0-beta', 'actionmailer': '= 3.0.0-beta', 'activerecord': '= 3.0.0-beta', 'railties': '= 3.0.0-beta'})
	source.add("rails", "3.0.0-beta1", deps={'activesupport': '= 3.0.0-beta1', 'actionpack': '= 3.0.0-beta1', 'actionmailer': '= 3.0.0-beta1', 'activerecord': '= 3.0.0-beta1', 'railties': '= 3.0.0-beta1'})

	check_solver_result(source, {"rack": "1.1"})

def test_pip_swapping_children_with_successors(source):
	source.root_dep("nginx", ">= 0.0.0")
	source.root_dep("build-essential", ">= 0.0.0")

	source.add("chef-handler", "1.3.0", deps={})
	source.add("yum", "3.10.0", deps={})
	source.add("windows", "1.39.2", deps={'chef-handler': '>= 0.0.0'})
	source.add("windows", "0.0.4", deps={'chef-handler': '>= 0.0.0'})
	source.add("windows", "0.0.3", deps={'chef-handler': '>= 0.0.0'})
	source.add("windows", "0.0.2", deps={'chef-handler': '>= 0.0.0'})
	source.add("windows", "0.0.1", deps={'chef-handler': '>= 0.0.0'})
	source.add("build-essential", "3.2.0", deps={'seven_zip': '>= 0.0.0'})
	source.add("build-essential", "2.4.0", deps={'7-zip': '>= 0.0.0'})
	source.add("7-zip", "1.0.0", deps={'windows': '>= 1.2.2'})
	source.add("nginx", "2.7.6", deps={'build-essential': '^2.0', 'yum-epel': '^1.3'})
	source.add("nginx", "0.1.0", deps={'build-essential': '^2.0'})
	source.add("nginx", "0.2.0", deps={'build-essential': '^2.0'})
	source.add("seven_zip", "2.0.0", deps={'windows': '>= 1.2.2'})
	source.add("yum-epel", "1.6.6", deps={'yum': '~3.10.0'})

	check_solver_result(source, {"chef-handler": "1.3.0", "yum": "3.10.0", "windows": "1.39.2", "build-essential": "2.4.0", "yum-epel": "1.6.6", "nginx": "2.7.6", "7-zip": "1.0.0"})

def test_pip_contiguous_grouping(source):
	source.root_dep("a", "*")
	source.root_dep("b", "*")

	source.add("a", "1.0.0", deps={})
	source.add("a", "1.0.1", deps={'c': '>= 0.0.0'})
	source.add("a", "1.0.2", deps={})
	source.add("b", "1.0.0", deps={'a': '!= 1.0.2'})
	source.add("c", "1.0.0", deps={})

	check_solver_result(source, {"a": "1.0.1", "b": "1.0.0", "c": "1.0.0"})

def test_pip_empty(source):

	source.add("rack-mount", "0.4", deps={})
	source.add("rack-mount", "0.5", deps={})
	source.add("rack-mount", "0.5.1", deps={})
	source.add("rack-mount", "0.5.2", deps={})
	source.add("rack-mount", "0.6", deps={})
	source.add("rack", "0.8", deps={})
	source.add("rack", "0.9", deps={})
	source.add("rack", "0.9.1", deps={})
	source.add("rack", "0.9.2", deps={})
	source.add("rack", "1.0", deps={})
	source.add("rack", "1.1", deps={})
	source.add("activemerchant", "1.2.3", deps={'activesupport': '>= 1.2.3'})
	source.add("activemerchant", "2.2.3", deps={'activesupport': '>= 2.2.3'})
	source.add("activemerchant", "2.3.5", deps={'activesupport': '>= 2.3.5'})
	source.add("actionmailer", "1.2.3", deps={'actionmailer': '= 1.2.3', 'activesupport': '= 1.2.3'})
	source.add("actionmailer", "2.2.3", deps={'actionmailer': '= 2.2.3', 'activesupport': '= 2.2.3'})
	source.add("actionmailer", "2.3.5", deps={'actionmailer': '= 2.3.5', 'activesupport': '= 2.3.5'})
	source.add("actionmailer", "3.0.0-beta", deps={'actionmailer': '= 3.0.0-beta', 'activesupport': '= 3.0.0-beta'})
	source.add("actionmailer", "3.0.0-beta1", deps={'actionmailer': '= 3.0.0-beta1', 'activesupport': '= 3.0.0-beta1'})
	source.add("railties", "1.2.3", deps={'activesupport': '= 1.2.3', 'actionpack': '= 1.2.3', 'actionmailer': '= 1.2.3', 'activerecord': '= 1.2.3'})
	source.add("railties", "2.2.3", deps={'activesupport': '= 2.2.3', 'actionpack': '= 2.2.3', 'actionmailer': '= 2.2.3', 'activerecord': '= 2.2.3'})
	source.add("railties", "2.3.5", deps={'activesupport': '= 2.3.5', 'actionpack': '= 2.3.5', 'actionmailer': '= 2.3.5', 'activerecord': '= 2.3.5'})
	source.add("railties", "3.0.0-beta", deps={})
	source.add("railties", "3.0.0-beta1", deps={})
	source.add("nokogiri", "1.0", deps={})
	source.add("nokogiri", "1.2", deps={})
	source.add("nokogiri", "1.2.1", deps={})
	source.add("nokogiri", "1.2.2", deps={})
	source.add("nokogiri", "1.3", deps={})
	source.add("nokogiri", "1.3.0-1", deps={})
	source.add("nokogiri", "1.3.5", deps={})
	source.add("nokogiri", "1.4.0", deps={})
	source.add("nokogiri", "1.4.2", deps={})
	source.add("weakling", "0.0.1", deps={})
	source.add("weakling", "0.0.2", deps={})
	source.add("weakling", "0.0.3", deps={})
	source.add("activesupport", "1.2.3", deps={})
	source.add("activesupport", "2.2.3", deps={})
	source.add("activesupport", "2.3.5", deps={})
	source.add("activesupport", "3.0.0-beta", deps={})
	source.add("activesupport", "3.0.0-beta1", deps={})
	source.add("actionpack", "1.2.3", deps={'activesupport': '= 1.2.3'})
	source.add("actionpack", "2.2.3", deps={'rack': '~0.9.0', 'activesupport': '= 2.2.3'})
	source.add("actionpack", "2.3.5", deps={'rack': '~1.0.0', 'activesupport': '= 2.3.5'})
	source.add("actionpack", "3.0.0-beta", deps={'rack-mount': '>= 0.5', 'rack': '~1.1', 'activesupport': '= 3.0.0-beta'})
	source.add("actionpack", "3.0.0-beta1", deps={'rack-mount': '>= 0.5', 'rack': '~1.1', 'activesupport': '= 3.0.0-beta1'})
	source.add("activerecord", "1.2.3", deps={'activesupport': '= 1.2.3'})
	source.add("activerecord", "2.2.3", deps={'activesupport': '= 2.2.3'})
	source.add("activerecord", "2.3.5", deps={'activesupport': '= 2.3.5'})
	source.add("activerecord", "3.0.0-beta", deps={'activesupport': '= 3.0.0-beta', 'arel': '>= 0.2'})
	source.add("activerecord", "3.0.0-beta1", deps={'activesupport': '= 3.0.0-beta1', 'arel': '>= 0.2'})
	source.add("rails", "3.0.0-beta", deps={'activesupport': '= 3.0.0-beta', 'actionpack': '= 3.0.0-beta', 'actionmailer': '= 3.0.0-beta', 'activerecord': '= 3.0.0-beta', 'railties': '= 3.0.0-beta'})
	source.add("rails", "3.0.0-beta1", deps={'activesupport': '= 3.0.0-beta1', 'actionpack': '= 3.0.0-beta1', 'actionmailer': '= 3.0.0-beta1', 'activerecord': '= 3.0.0-beta1', 'railties': '= 3.0.0-beta1'})

	check_solver_result(source, {})

def test_pip_simple_with_shared_dependencies(source):
	source.root_dep("actionpack", "*")
	source.root_dep("activerecord", "2.3.5")

	source.add("rack-mount", "0.4", deps={})
	source.add("rack-mount", "0.5", deps={})
	source.add("rack-mount", "0.5.1", deps={})
	source.add("rack-mount", "0.5.2", deps={})
	source.add("rack-mount", "0.6", deps={})
	source.add("rack", "0.8", deps={})
	source.add("rack", "0.9", deps={})
	source.add("rack", "0.9.1", deps={})
	source.add("rack", "0.9.2", deps={})
	source.add("rack", "1.0", deps={})
	source.add("rack", "1.1", deps={})
	source.add("activemerchant", "1.2.3", deps={'activesupport': '>= 1.2.3'})
	source.add("activemerchant", "2.2.3", deps={'activesupport': '>= 2.2.3'})
	source.add("activemerchant", "2.3.5", deps={'activesupport': '>= 2.3.5'})
	source.add("actionmailer", "1.2.3", deps={'actionmailer': '= 1.2.3', 'activesupport': '= 1.2.3'})
	source.add("actionmailer", "2.2.3", deps={'actionmailer': '= 2.2.3', 'activesupport': '= 2.2.3'})
	source.add("actionmailer", "2.3.5", deps={'actionmailer': '= 2.3.5', 'activesupport': '= 2.3.5'})
	source.add("actionmailer", "3.0.0-beta", deps={'actionmailer': '= 3.0.0-beta', 'activesupport': '= 3.0.0-beta'})
	source.add("actionmailer", "3.0.0-beta1", deps={'actionmailer': '= 3.0.0-beta1', 'activesupport': '= 3.0.0-beta1'})
	source.add("railties", "1.2.3", deps={'activesupport': '= 1.2.3', 'actionpack': '= 1.2.3', 'actionmailer': '= 1.2.3', 'activerecord': '= 1.2.3'})
	source.add("railties", "2.2.3", deps={'activesupport': '= 2.2.3', 'actionpack': '= 2.2.3', 'actionmailer': '= 2.2.3', 'activerecord': '= 2.2.3'})
	source.add("railties", "2.3.5", deps={'activesupport': '= 2.3.5', 'actionpack': '= 2.3.5', 'actionmailer': '= 2.3.5', 'activerecord': '= 2.3.5'})
	source.add("railties", "3.0.0-beta", deps={})
	source.add("railties", "3.0.0-beta1", deps={})
	source.add("nokogiri", "1.0", deps={})
	source.add("nokogiri", "1.2", deps={})
	source.add("nokogiri", "1.2.1", deps={})
	source.add("nokogiri", "1.2.2", deps={})
	source.add("nokogiri", "1.3", deps={})
	source.add("nokogiri", "1.3.0-1", deps={})
	source.add("nokogiri", "1.3.5", deps={})
	source.add("nokogiri", "1.4.0", deps={})
	source.add("nokogiri", "1.4.2", deps={})
	source.add("weakling", "0.0.1", deps={})
	source.add("weakling", "0.0.2", deps={})
	source.add("weakling", "0.0.3", deps={})
	source.add("activesupport", "1.2.3", deps={})
	source.add("activesupport", "2.2.3", deps={})
	source.add("activesupport", "2.3.5", deps={})
	source.add("activesupport", "3.0.0-beta", deps={})
	source.add("activesupport", "3.0.0-beta1", deps={})
	source.add("actionpack", "1.2.3", deps={'activesupport': '= 1.2.3'})
	source.add("actionpack", "2.2.3", deps={'rack': '~0.9.0', 'activesupport': '= 2.2.3'})
	source.add("actionpack", "2.3.5", deps={'rack': '~1.0.0', 'activesupport': '= 2.3.5'})
	source.add("actionpack", "3.0.0-beta", deps={'rack-mount': '>= 0.5', 'rack': '~1.1', 'activesupport': '= 3.0.0-beta'})
	source.add("actionpack", "3.0.0-beta1", deps={'rack-mount': '>= 0.5', 'rack': '~1.1', 'activesupport': '= 3.0.0-beta1'})
	source.add("activerecord", "1.2.3", deps={'activesupport': '= 1.2.3'})
	source.add("activerecord", "2.2.3", deps={'activesupport': '= 2.2.3'})
	source.add("activerecord", "2.3.5", deps={'activesupport': '= 2.3.5'})
	source.add("activerecord", "3.0.0-beta", deps={'activesupport': '= 3.0.0-beta', 'arel': '>= 0.2'})
	source.add("activerecord", "3.0.0-beta1", deps={'activesupport': '= 3.0.0-beta1', 'arel': '>= 0.2'})
	source.add("rails", "3.0.0-beta", deps={'activesupport': '= 3.0.0-beta', 'actionpack': '= 3.0.0-beta', 'actionmailer': '= 3.0.0-beta', 'activerecord': '= 3.0.0-beta', 'railties': '= 3.0.0-beta'})
	source.add("rails", "3.0.0-beta1", deps={'activesupport': '= 3.0.0-beta1', 'actionpack': '= 3.0.0-beta1', 'actionmailer': '= 3.0.0-beta1', 'activerecord': '= 3.0.0-beta1', 'railties': '= 3.0.0-beta1'})

	check_solver_result(source, {"actionpack": "2.3.5", "activesupport": "2.3.5", "rack": "1.0", "activerecord": "2.3.5"})

def test_pip_previous_conflict(source):
	source.root_dep("a", "*")
	source.root_dep("b", "*")

	source.add("a", "0.3.0", deps={'c': '~1.4', 'e': '~1.4'})
	source.add("a", "0.2.0", deps={'c': '~1.3', 'e': '~1.4'})
	source.add("a", "0.1.0", deps={'c': '>= 0', 'f': '~1.4', 'e': '~1.0'})
	source.add("c", "2.0.0", deps={'d': '~2.0.0'})
	source.add("c", "1.4.0", deps={'d': '~1.4'})
	source.add("f", "1.4.0", deps={'e': '~2.0'})
	source.add("d", "1.4.0", deps={})
	source.add("d", "2.0.0", deps={})
	source.add("e", "2.0.0", deps={'d': '> 1, < 3'})
	source.add("e", "1.4.0", deps={'d': '> 1, < 3'})
	source.add("e", "1.0.0", deps={})
	source.add("b", "2.0.0", deps={'c': '= 2.0.0', 'd': '~2.0'})
	source.add("b", "1.4.0", deps={'c': '= 1.4.0', 'd': '~1.4'})

	check_solver_result(source, {"a": "0.3.0", "c": "1.4.0", "e": "1.4.0", "d": "1.4.0", "b": "1.4.0"})

def test_pip_conflict_on_child(source):
	source.root_dep("chef_app", "*")

	source.add("chef_app", "1.0.0", deps={'chef': '~10.26', 'berkshelf': '~2.0'})
	source.add("chef", "10.26.0", deps={'json': '<= 1.7.7, >= 1.4.4'})
	source.add("berkshelf", "2.0.7", deps={'json': '>= 1.7.7'})
	source.add("json", "1.6.5", deps={})
	source.add("json", "1.7.7", deps={})
	source.add("json", "1.8.0", deps={})

	check_solver_result(source, {"chef_app": "1.0.0", "chef": "10.26.0", "berkshelf": "2.0.7", "json": "1.7.7"})


def test_pip_conflict(source):
	source.root_dep("my_app", "*")

	source.add("my_app", "1.0.0", deps={'activemodel': '>= 0', 'grape': '>= 0'})
	source.add("activemodel", "3.2.8", deps={'builder': '~3.0.0'})
	source.add("activemodel", "3.2.9", deps={'builder': '~3.0.0'})
	source.add("activemodel", "3.2.10", deps={'builder': '~3.0.0'})
	source.add("activemodel", "3.2.11", deps={'builder': '~3.0.0'})
	source.add("builder", "3.0.4", deps={})
	source.add("builder", "3.1.4", deps={})
	source.add("grape", "0.2.6", deps={'builder': '>= 0'})

	check_solver_result(source, {"activemodel": "3.2.11", "my_app": "1.0.0", "builder": "3.0.4", "grape": "0.2.6"})

def test_pip_root_conflict_on_child(source):
	source.root_dep("activesupport", "~3.0")
	source.root_dep("i18n", "~0.4")
	source.root_dep("activerecord", "~3.0")
	source.root_dep("builder", "~2.1.2")

	source.add("activemodel", "3.0.5", deps={'activesupport': '= 3.0.5', 'builder': '~2.1.2', 'i18n': '~0.4'})
	source.add("activemodel", "3.0.0", deps={'activesupport': '= 3.0.0', 'builder': '~2.1.2', 'i18n': '~0.4.1'})
	source.add("activemodel", "3.1.3", deps={'activesupport': '= 3.1.3', 'builder': '~2.1.2', 'i18n': '~0.5'})
	source.add("activesupport", "3.0.0", deps={})
	source.add("activesupport", "3.0.1", deps={})
	source.add("activesupport", "3.0.5", deps={})
	source.add("activesupport", "3.1.7", deps={})
	source.add("builder", "2.1.2", deps={})
	source.add("builder", "3.0.1", deps={})
	source.add("builder", "3.1.3", deps={})
	source.add("activerecord", "3.0.0", deps={'activemodel': '= 3.0.0', 'activesupport': '= 3.0.0'})
	source.add("activerecord", "3.0.5", deps={'activemodel': '= 3.0.5', 'activesupport': '= 3.0.5'})
	source.add("activerecord", "3.0.9", deps={'activemodel': '= 3.1.5', 'activesupport': '= 3.1.5'})
	source.add("i18n", "0.4.1", deps={})
	source.add("i18n", "0.4.2", deps={})

	check_solver_result(source, {"activemodel": "3.0.5", "activesupport": "3.0.5", "i18n": "0.4.2", "activerecord": "3.0.5", "builder": "2.1.2"})

def test_pip_previous_primary_conflict(source):
	source.root_dep("a", ">= 4.2")
	source.root_dep("b", "< 5.1")

	source.add("a", "5.1.0", deps={})
	source.add("a", "5.0.5", deps={'c': '*'})
	source.add("a", "5.0.4", deps={})
	source.add("a", "4.0.3", deps={'c': '*'})
	source.add("a", "4.0.2", deps={})
	source.add("a", "4.0.1", deps={'c': '*'})
	source.add("b", "5.1.0", deps={'a': '= 5.1.0'})
	source.add("b", "5.0.5", deps={'a': '= 5.0.5'})
	source.add("b", "5.0.4", deps={'a': '= 5.0.4'})
	source.add("c", "1.0.0", deps={})

	check_solver_result(source, {"a": "5.0.5", "c": "1.0.0", "b": "5.0.5"})

def test_pip_complex_conflict(source):
	source.root_dep("my_app", "*")

	source.add("a", "1.0.2", deps={'d': '>= 0'})
	source.add("a", "1.1.4", deps={'d': '>= 0'})
	source.add("a", "1.2.0", deps={'d': '>= 0'})
	source.add("a", "1.4.0", deps={'d': '>= 0'})
	source.add("b", "0.3.4", deps={'a': '>= 1.5.0'})
	source.add("b", "0.3.5", deps={'a': '>= 1.2'})
	source.add("b", "0.3.3", deps={'a': '> 1.0'})
	source.add("my_app", "1.3.0", deps={'c': '>= 4.0', 'b': '>= 0'})
	source.add("my_app", "1.2.0", deps={'c': '~3.3.0', 'b': '= 0.3.4'})
	source.add("my_app", "1.1.0", deps={'c': '~3.2.0', 'b': '= 0.3.5'})
	source.add("d", "1.3.0", deps={'x': '>= 0'})
	source.add("d", "1.4.1", deps={'x': '>= 0'})
	source.add("d", "0.9.8", deps={})
	source.add("c", "3.2", deps={'a': '^1.0'})
	source.add("c", "3.3", deps={'a': '^1.0'})

	check_solver_result(source, {"a": "1.4.0", "b": "0.3.5", "my_app": "1.1.0", "d": "0.9.8", "c": "3.2"})

def test_pip_simple_speed_test(source):
	source.root_dep("menu", ">= 1.0.0")
	source.root_dep("icons", "1.0.0")

	source.add("dropdown", "2.3.0", deps={'icons': '2.0.0'})
	source.add("dropdown", "2.2.0", deps={'icons': '2.0.0'})
	source.add("dropdown", "2.1.0", deps={'icons': '2.0.0'})
	source.add("dropdown", "2.0.0", deps={'icons': '2.0.0'})
	source.add("dropdown", "1.8.0", deps={})
	source.add("menu", "1.5.0", deps={'dropdown': '>= 2.0.0'})
	source.add("menu", "1.4.0", deps={'dropdown': '>= 2.0.0'})
	source.add("menu", "1.3.0", deps={'dropdown': '>= 2.0.0'})
	source.add("menu", "1.2.0", deps={'dropdown': '>= 2.0.0'})
	source.add("menu", "1.1.0", deps={'dropdown': '>= 2.0.0'})
	source.add("menu", "1.0.0", deps={'dropdown': '1.8.0'})
	source.add("icons", "2.0.0", deps={})
	source.add("icons", "1.0.0", deps={})

	check_solver_result(source, {"dropdown": "1.8.0", "menu": "1.0.0", "icons": "1.0.0"})

def test_pip_overlap(source):
	source.root_dep("a", "1.0.0")
	source.root_dep("b", "1.0.0")

	source.add("a", "1.0.0", deps={'shared': '< 4.0.0'})
	source.add("b", "1.0.0", deps={'shared': '< 5.0.0'})
	source.add("shared", "2.0.0", deps={})
	source.add("shared", "3.0.0", deps={})
	source.add("shared", "3.6.9", deps={})
	source.add("shared", "4.0.0", deps={})
	source.add("shared", "5.0.0", deps={})

	check_solver_result(source, {"a": "1.0.0", "shared": "3.6.9", "b": "1.0.0"})

def test_pip_simple_with_dependencies(source):
	source.root_dep("actionpack", "*")

	source.add("rack-mount", "0.4", deps={})
	source.add("rack-mount", "0.5", deps={})
	source.add("rack-mount", "0.5.1", deps={})
	source.add("rack-mount", "0.5.2", deps={})
	source.add("rack-mount", "0.6", deps={})
	source.add("rack", "0.8", deps={})
	source.add("rack", "0.9", deps={})
	source.add("rack", "0.9.1", deps={})
	source.add("rack", "0.9.2", deps={})
	source.add("rack", "1.0", deps={})
	source.add("rack", "1.1", deps={})
	source.add("activemerchant", "1.2.3", deps={'activesupport': '>= 1.2.3'})
	source.add("activemerchant", "2.2.3", deps={'activesupport': '>= 2.2.3'})
	source.add("activemerchant", "2.3.5", deps={'activesupport': '>= 2.3.5'})
	source.add("actionmailer", "1.2.3", deps={'actionmailer': '= 1.2.3', 'activesupport': '= 1.2.3'})
	source.add("actionmailer", "2.2.3", deps={'actionmailer': '= 2.2.3', 'activesupport': '= 2.2.3'})
	source.add("actionmailer", "2.3.5", deps={'actionmailer': '= 2.3.5', 'activesupport': '= 2.3.5'})
	source.add("actionmailer", "3.0.0-beta", deps={'actionmailer': '= 3.0.0-beta', 'activesupport': '= 3.0.0-beta'})
	source.add("actionmailer", "3.0.0-beta1", deps={'actionmailer': '= 3.0.0-beta1', 'activesupport': '= 3.0.0-beta1'})
	source.add("railties", "1.2.3", deps={'activesupport': '= 1.2.3', 'actionpack': '= 1.2.3', 'actionmailer': '= 1.2.3', 'activerecord': '= 1.2.3'})
	source.add("railties", "2.2.3", deps={'activesupport': '= 2.2.3', 'actionpack': '= 2.2.3', 'actionmailer': '= 2.2.3', 'activerecord': '= 2.2.3'})
	source.add("railties", "2.3.5", deps={'activesupport': '= 2.3.5', 'actionpack': '= 2.3.5', 'actionmailer': '= 2.3.5', 'activerecord': '= 2.3.5'})
	source.add("railties", "3.0.0-beta", deps={})
	source.add("railties", "3.0.0-beta1", deps={})
	source.add("nokogiri", "1.0", deps={})
	source.add("nokogiri", "1.2", deps={})
	source.add("nokogiri", "1.2.1", deps={})
	source.add("nokogiri", "1.2.2", deps={})
	source.add("nokogiri", "1.3", deps={})
	source.add("nokogiri", "1.3.0-1", deps={})
	source.add("nokogiri", "1.3.5", deps={})
	source.add("nokogiri", "1.4.0", deps={})
	source.add("nokogiri", "1.4.2", deps={})
	source.add("weakling", "0.0.1", deps={})
	source.add("weakling", "0.0.2", deps={})
	source.add("weakling", "0.0.3", deps={})
	source.add("activesupport", "1.2.3", deps={})
	source.add("activesupport", "2.2.3", deps={})
	source.add("activesupport", "2.3.5", deps={})
	source.add("activesupport", "3.0.0-beta", deps={})
	source.add("activesupport", "3.0.0-beta1", deps={})
	source.add("actionpack", "1.2.3", deps={'activesupport': '= 1.2.3'})
	source.add("actionpack", "2.2.3", deps={'rack': '~0.9.0', 'activesupport': '= 2.2.3'})
	source.add("actionpack", "2.3.5", deps={'rack': '~1.0.0', 'activesupport': '= 2.3.5'})
	source.add("activerecord", "1.2.3", deps={'activesupport': '= 1.2.3'})
	source.add("activerecord", "2.2.3", deps={'activesupport': '= 2.2.3'})
	source.add("activerecord", "2.3.5", deps={'activesupport': '= 2.3.5'})

	check_solver_result(source, {"actionpack": "2.3.5", "activesupport": "2.3.5", "rack": "1.0"})

def test_pip_three_way_conflict(source):
	source.root_dep("AFOAuth2Client", "*")
	source.root_dep("AFAmazonS3Client", "*")
	source.root_dep("CargoBay", "*")

	source.add("AFOAuth2Client", "0.1.2", deps={'AFNetworking': '^1.3'})
	source.add("AFOAuth2Client", "0.1.1", deps={'AFNetworking': '^1.0'})
	source.add("AFOAuth2Client", "0.1.0", deps={'AFNetworking': '^1.0'})
	source.add("AFOAuth2Client", "0.0.1", deps={'AFNetworking': '^1.0'})
	source.add("AFAmazonS3Client", "2.0.0", deps={'AFNetworking': '^2.0'})
	source.add("AFAmazonS3Client", "1.0.1", deps={'AFNetworking': '^1.3'})
	source.add("AFAmazonS3Client", "0.3.0", deps={'AFNetworking': '^1.0'})
	source.add("AFAmazonS3Client", "0.2.0", deps={'AFNetworking': '^1.0'})
	source.add("AFAmazonS3Client", "0.1.0", deps={'AFNetworking': '^1.0'})
	source.add("CargoBay", "2.1.0", deps={'AFNetworking': '^2.2'})
	source.add("CargoBay", "2.0.3", deps={'AFNetworking': '^2.1'})
	source.add("CargoBay", "2.0.2", deps={'AFNetworking': '^2.0'})
	source.add("CargoBay", "2.0.1", deps={'AFNetworking': '^2.0'})
	source.add("CargoBay", "2.0.0", deps={'AFNetworking': '^2.0'})
	source.add("CargoBay", "1.0.0", deps={'AFNetworking': '^1.0'})
	source.add("CargoBay", "0.3.3", deps={'AFNetworking': '>= 1.0'})
	source.add("CargoBay", "0.3.2", deps={'AFNetworking': '>= 1.0'})
	source.add("CargoBay", "0.3.1", deps={'AFNetworking': '>= 1.0'})
	source.add("CargoBay", "0.3.0", deps={'AFNetworking': '>= 1.0'})
	source.add("CargoBay", "0.2.1", deps={'AFNetworking': '>= 0.9'})
	source.add("CargoBay", "0.2.0", deps={'AFNetworking': '>= 0.9'})
	source.add("CargoBay", "0.1.0", deps={'AFNetworking': '>= 0.9'})
	source.add("AFNetworking", "2.5.0", deps={})
	source.add("AFNetworking", "2.4.1", deps={})
	source.add("AFNetworking", "2.4.0", deps={})
	source.add("AFNetworking", "2.3.1", deps={})
	source.add("AFNetworking", "2.3.0", deps={})
	source.add("AFNetworking", "2.2.4", deps={})
	source.add("AFNetworking", "2.2.3", deps={})
	source.add("AFNetworking", "2.2.2", deps={})
	source.add("AFNetworking", "2.2.1", deps={})
	source.add("AFNetworking", "2.2.0", deps={})
	source.add("AFNetworking", "2.1.0", deps={})
	source.add("AFNetworking", "2.0.3", deps={})
	source.add("AFNetworking", "2.0.2", deps={})
	source.add("AFNetworking", "2.0.1", deps={})
	source.add("AFNetworking", "2.0.0", deps={})
	source.add("AFNetworking", "1.3.4", deps={})
	source.add("AFNetworking", "1.3.3", deps={})
	source.add("AFNetworking", "1.3.2", deps={})
	source.add("AFNetworking", "1.3.1", deps={})
	source.add("AFNetworking", "1.3.0", deps={})
	source.add("AFNetworking", "1.2.1", deps={})
	source.add("AFNetworking", "1.2.0", deps={})
	source.add("AFNetworking", "1.1.0", deps={})
	source.add("AFNetworking", "1.0.1", deps={})
	source.add("AFNetworking", "1.0", deps={})
	source.add("AFNetworking", "0.10.1", deps={})
	source.add("AFNetworking", "0.10.0", deps={})
	source.add("AFNetworking", "0.9.2", deps={})
	source.add("AFNetworking", "0.9.1", deps={})
	source.add("AFNetworking", "0.9.0", deps={})
	source.add("AFNetworking", "0.7.0", deps={'JSONKit': '>= 0'})
	source.add("AFNetworking", "0.5.1", deps={'JSONKit': '>= 0'})

	check_solver_result(source, {"AFOAuth2Client": "0.1.2", "AFAmazonS3Client": "1.0.1", "CargoBay": "1.0.0", "AFNetworking": "1.3.4"})