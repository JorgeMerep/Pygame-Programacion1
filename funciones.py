# Función para renderizar texto centrado
def render_texto(texto, fuente, color, superficie, centro):
    render = fuente.render(texto, True, color)
    rect = render.get_rect(center=centro)
    superficie.blit(render, rect)