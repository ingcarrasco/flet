from xhtml2pdf import pisa

def convert_html_to_pdf(html_string, pdf_path):
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)
        
    return not pisa_status.err

# HTML content
html_content = '''
<!DOCTYPE html>
<html>
<head>
<style>
div {
  width: 100%;
  border: 1px solid black;
  padding: 50px;
  margin: 20px;
}
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 0px;
  text-align: left;
  padding: 1px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>

<h2 style='text-align: center'>Carta responsiva</h2>

<table>
  <tr>
    <th>Departamento</th>
    <th style='text-align: center'>Persona responsable</th>
    <th style='text-align: right'>Departamento de Sistemas</th>
  </tr>
  <tr>
    <td>Compras</td>
    <td style='text-align: center'>Niccolo di Bernardo dei Machiavelli</td>
    <td style='text-align: right'>Carta responsiva:</td>
  </tr>
  <tr>
    <td>Gerente de compras</td>
    <td> </td>
    <td style='text-align: right'>098129021908</td>
  </tr>
</table>

<p>
<b>Lugar de trabajo</b><br>
Corporativo
</p>

<p>
<b>Fecha de entrega: </b> 11 de marzo de 2024
<br>
<b>Lugar de entrega: </b> Zapopan, Jalisco
<br>
<b>Fecha de devolución: </b> Cuando se requerida por el departamento de sistemas
</p>
<br>
<table>
    <tr>
        <th>Tipo</th>
        <th>Marca</th>
        <th>Modelo</th>
        <th>Serie</th>
        <th>IMEI</th>
        <th>Precio</th>
    </tr>
    <tr>
        <td>Laptop</td>
        <td>Apple</td>
        <td>Macbook Air M1, 2020</td>
        <td>XXXXXXXXX</td>
        <td> </td>
        <td>$ 24,987.00</td>
    </tr>
</table>
<br><br><br><br><br><br><br>
<p align='justify'>
La utilización de los equipos es para uso exclusivo de mis funciones dentro de la empresa, mismas que podrán ser solicitadas y deberán ser devueltas en cualquier momento por el departamento de Capital Humano en cualquiera de los siguientes casos que de manera enunciativa pero no limitativa se mencionan:
<br>• En caso de hacer mal uso del equipo
<br>• En caso de que la empresa lo considere necesario
<br>• Terminación voluntaria de la relación laboral
<br>• Rescisión de Contrato de igual manera, me comprometo y asumo que seré el responsable del adecuado y buen uso del mismo.
<br> Asimismo, en caso de robo o extravío tendré que avisar inmediatamente al departamento de Capital Humano y/o Gerencia Administrativa para tomar las medidas que sean necesarias. En el supuesto de maltrato del equipo y que por negligencia ocasionara la pérdida funcional total o descompostura del mismo, tendré que pagar el costo de la compostura o piezas de reposición.
</p>
<br><br><br><br>
<table>
    <tr>
        <th style='text-align: center'>_________________________________________________</th>
        <th style='text-align: center'>_________________________________________________</th>

    </tr>
    <tr>
        <td style='text-align: center'>Niccolo di Bernardo dei Machiavelli</td>
        <td style='text-align: center'>Friedrich Wilhelm Nietzsche</td>
    </tr>
</table>

<p><b>Observaciones:</b> Con mi firma hago constancia de que recibí mis archivos y correos electrónicos completos.</p>
<p>El software instalado es el único autorizado para su uso, cualquier instalación adicional deberá ser autorizada por escrito por el departamento de Sistemas, en caso contrario, cualquier violación a los derechos de propiedad intelectual serán responsabilidad de quien recibe.</p>
<hr>
<p>
Fecha de devolución: ______________________________
<br>Reviso el equipo: _________________________________
</p>

<br>
<b>Observaciones:</b>
<div>
<br>
</div>

<p>Importe de cargo: $_____________________________ 
<br>Recibe: _______________________________________
</p>


</body>
</html>
'''

# Generate PDF
pdf_path = "./example.pdf"
if convert_html_to_pdf(html_content, pdf_path):
    print(f"PDF generated and saved at {pdf_path}")
else:
    print("PDF generation failed")