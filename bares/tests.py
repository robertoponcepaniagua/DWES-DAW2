from django.test import TestCase


class BaresViewsTests(TestCase):
    def test_inspector_displays_request_data(self):
        response = self.client.get("/inspector/?nombre=Ada")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "GET:    {'nombre': ['Ada']}")

    def test_buscar_handles_empty_and_repeated_parameters(self):
        empty_response = self.client.get("/bares/buscar/")
        repeated_response = self.client.get(
            "/bares/buscar/?q=CAMARONES&q=otro"
        )

        self.assertContains(empty_response, "Escribe un término de búsqueda")
        self.assertContains(repeated_response, "Buscando «camarones»...")
        self.assertContains(repeated_response, "parámetro q llegó repetido")

    def test_buscar_escapes_query_and_detalle_returns_404_when_missing(self):
        search_response = self.client.get(
            "/bares/buscar/?q=%3Cscript%3E"
        )
        missing_bar_response = self.client.get("/bares/99/")

        self.assertContains(search_response, "&lt;script&gt;")
        self.assertEqual(missing_bar_response.status_code, 404)
