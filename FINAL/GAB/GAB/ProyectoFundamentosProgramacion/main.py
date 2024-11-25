from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Muestra la página principal con el formulario
    return render_template('index.html', resultado=None)

@app.route('/calcular_ahorros', methods=['GET', 'POST'])
def calcular_ahorros():
    try:
        # Inicializar variables
        income = 0
        expenses = 0
        savings_goal = 0
        resultado = None

        if request.method == 'POST':
            # Obtener los datos enviados por POST
            income = float(request.form['income'])
            expenses = float(request.form['expenses'])
            savings_goal = float(request.form['savings_goal'])
        elif request.method == 'GET':
            # Obtener los datos enviados por GET
            income = float(request.args.get('income', 0))
            expenses = float(request.args.get('expenses', 0))
            savings_goal = float(request.args.get('savings_goal', 0))

        # Validar los datos
        if income <= 0 or expenses <= 0 or savings_goal <= 0:
            resultado = 'Por favor, introduce valores positivos en todos los campos.'
        else:
            # Calcular el ahorro mensual y los meses necesarios para alcanzar la meta
            ahorro_mensual = income - expenses
            if ahorro_mensual <= 0:
                resultado = 'No es posible ahorrar con los gastos actuales. Reduce tus gastos o aumenta tus ingresos.'
            else:
                meses_necesarios = savings_goal / ahorro_mensual
                meses_necesarios = int(meses_necesarios) if meses_necesarios.is_integer() else int(meses_necesarios) + 1
                resultado = f'Con un ahorro mensual de S/{ahorro_mensual:.2f}, alcanzarás tu meta en aproximadamente {meses_necesarios} meses.'

        # Renderizar la página con el resultado
        return render_template('index.html', resultado=resultado)

    except Exception as e:
        # Manejar errores y mostrar mensaje
        return render_template('index.html', resultado=f'Error: {str(e)}')
@app.route('/pagina1')
def pagina1():
    return render_template('pagina1.html')
if __name__ == '__main__':
    app.run(debug=True)