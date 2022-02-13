#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, task
from plantuml import PlantUML
from os.path import abspath

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "PhysicsSandbox"
default_task = ["create_uml_diagrams", "publish"]


@init
def set_properties(project):
    project.build_depends_on("pymunk")
    project.depends_on('plantuml')
    project.set_property('coverage_break_build', False)


# create UML documentation
@task("create_uml_diagrams", description="create the UML diagram images based of the PlantUML code")
def create_uml_diagrams():
    # create a server object to call for your computations
    server = PlantUML(url='http://www.plantuml.com/plantuml/img/',
                      basic_auth={},
                      form_auth={}, http_opts={}, request_opts={})

    # Send and compile your diagram files to/with the PlantUML server
    server.processes_file(abspath('docs/uml/class_diagram.puml'))
    server.processes_file(abspath('docs/uml/use_case_diagram.puml'))
    server.processes_file(abspath('docs/uml/activity_diagram.puml'))
