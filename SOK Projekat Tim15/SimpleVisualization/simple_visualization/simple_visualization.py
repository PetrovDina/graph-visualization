from core_django_app.services.services import VisualizeService
import pkg_resources

class SimpleVisualization(VisualizeService):

    def plugin_id(self):
        return "SimpleVisualization"

    def name(self):
        return "SimpleVisualization"

    def visualize(self):
        pom = pkg_resources.resource_string(__name__, "simple_visualize_graph.js")
        return str(pom, "UTF-8")