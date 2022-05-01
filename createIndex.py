#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:00:29 2022

@author: fernandasanchez
"""

import pandas as pd
from airium import Airium

dpf = {} #DESARROLLO DE PROTOTIPO FISICO
dps = {} #DESARROLLO DE PROTOTIPO DE SOFTWARE
idpm = {} #INVESTIGACION Y DESARROLLO DE PROPUESTAS DE MEJORA
psebt = {} #PRODUCTOS O SERVICIOS PARA EMPRENDIMIENTO DE BASE TECNOLOGICA


def loadProjects():

    file_name = 'proyectos registrados final 2-11-2021.xlsx'
    sheet =  0
    
    df = pd.read_excel(io=file_name, sheet_name=sheet)
    for index, row in df.iterrows():
        if row['ACCEPTADO'] == 'AC':
            if row['TIPO DE PROYECTO'] ==  'DESARROLLO DE PROTOTIPO FISICO':
                if row['ENFOQUE_SOCIAL'] == 'SI':
                    dpf[row['ID']] = [row['NOMBRE DEL PROYECTO'], True]
                else:   
                    dpf[row['ID']] = [row['NOMBRE DEL PROYECTO'], False]

            if row['TIPO DE PROYECTO'] ==  'DESARROLLO DE PROTOTIPO DE SOFTWARE':
                if row['ENFOQUE_SOCIAL'] == 'SI':
                    dps[row['ID']] = [row['NOMBRE DEL PROYECTO'], True]
                else:
                    dps[row['ID']] = [row['NOMBRE DEL PROYECTO'], False]

            if row['TIPO DE PROYECTO'] ==  'INVESTIGACION Y DESARROLLO DE PROPUESTAS DE MEJORA':
                if row['ENFOQUE_SOCIAL'] == 'SI':
                    idpm[row['ID']] = [row['NOMBRE DEL PROYECTO'], True]
                else:
                    idpm[row['ID']] = [row['NOMBRE DEL PROYECTO'], False]

            if row['TIPO DE PROYECTO'] ==  'PRODUCTOS O SERVICIOS PARA EMPRENDIMIENTO DE BASE TECNOLOGICA':
                if row['ENFOQUE_SOCIAL'] == 'SI':
                    psebt[row['ID']] = [row['NOMBRE DEL PROYECTO'], True]
                else:
                    psebt[row['ID']] = [row['NOMBRE DEL PROYECTO'], False]
            

def outputHTML():
   

    a = Airium()

    
    a('<!DOCTYPE html>')
    with a.html(lang="pl"):
        with a.head():
            a.meta(charset="utf-8")
            a.title(_t="Muestra Virtual")
            a.link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css')
            a.link(rel='stylesheet', href='assets/css/indice.css')
            a.link(rel='preconnect', href='https://fonts.googleapis.com')
            a.link(rel='preconnect', href='https://fonts.gstatic.com')
            a.link(href='https://fonts.googleapis.com/css2?family=Raleway:wght@200&display=swap', rel='stylesheet')
            a.link(rel='icon', href='assets/img/Screen Shot 2022-04-03 at 17.10.51.png')
    
        with a.body():
            with a.div(klass="container-fluid"):
                with a.nav(klass='navbar navbar-expand-sm justify-content-center'):
                    with a.a(klass='navbar-brand',href="#"):
                         a.img(src='/assets/img/logoExpoTec.png', width='500px')
                with a.div(klass='jumbotron text-center'):
                    with a.h1():
                        a('Bienvenidos a la muestra virtual del evento ExpoIngenierías #18')
                    with a.h2():
                        a('Escuela de Ingeniería y Ciencias Región Monterrey Tecnológico de Monterrey')
                    a.br()
                    with a.p(id='desc'):
                        a('ExpoIngenierías es el evento de difusión que realiza la Escuela de Ingeniería y Ciencias al final de cada semestre, en donde se exponen los mejores proyectos generados en sus cursos, que resuelven problemas de ingeniería y ciencias aplicados a la industria y/o a la sociedad.')
                        a.br()
                        a.br()
                        a('A continuación se muestran los proyectos agrupados por la categoría a la que pertenecen:')
                    with a.h4():
                        a("Categorias:")
                    with a.h5():
                        with a.a(href="#dpf"):
                            a("DESARROLLO DE PROTOTIPO FISICO")
                    with a.h5():
                        with a.a(href="#dps"):
                            a("DESARROLLO DE PROTOTIPO DE SOFTWARE")
                    with a.h5():
                        with a.a(href="#idpm"):
                            a("INVESTIGACION Y DESARROLLO DE PROPUESTAS DE MEJORA")
                    with a.h5():
                        with a.a(href="#psebt"):
                            a("PRODUCTOS O SERVICIOS PARA EMPRENDIMIENTO DE BASE TECNOLOGICA")
            with a.div(klass='container'):
                with a.dl():
                    with a.dt(id="dpf"):
                        a('DESARROLLO DE PROTOTIPO FISICO')
                        for id, proyecto in dpf.items():
                            with a.dd():
                                if proyecto[1]:
                                    with a.a(href='proyectos/Proyecto_' + str(id) + '.html', target='_blank'):
                                        a('&#9642 ' + proyecto[0] + ' &#8212;')
                                        with a.p(klass="badge badge-success"):
                                                a(" Con Enfoque Social")
                                else:
                                    with a.a(href='proyectos/Proyecto_' + str(id) + '.html', target='_blank'):
                                        a('&#9642 ' + proyecto[0])
                    with a.div(klass="text-center"):
                        with a.a(href="#desc", klass="btn btn-outline-secondary", type="button"):
                            a("Ver Categorías")
                    a.br()
                    a.br()
                    with a.dt(id="dps"):
                        a('DESARROLLO DE PROTOTIPO SOFTWARE')
                        for id, proyecto in dps.items():
                            with a.dd():
                                if proyecto[1]:
                                    with a.a(href='proyectos/Proyecto_' + str(id) + '.html', target='_blank'):
                                        a('&#9642 ' + proyecto[0] +' &#8212;')
                                        with a.p(klass="badge badge-success"):
                                                a("Con Enfoque Social")
                                else:
                                    with a.a(href='proyectos/Proyecto_' + str(id) + '.html', target='_blank'):
                                        a('&#9642 ' + proyecto[0])
                    with a.div(klass="text-center"):
                        with a.a(href="#desc", klass="btn btn-outline-secondary", type="button"):
                            a("Ver Categorías")
                    a.br()
                    a.br()
                    with a.dt(id="idpm"):
                        a('INVESTIGACION Y DESARROLLO DE PROPUESTAS DE MEJORA')
                        for id, proyecto in idpm.items():
                            with a.dd():
                                if proyecto[1]:
                                    with a.a(href='proyectos/Proyecto_' + str(id) + '.html', target='_blank'):
                                        a('&#9642 ' + proyecto[0] + ' &#8212;')
                                        with a.p(klass="badge badge-success"):
                                                a("Con Enfoque Social")
                                else:
                                    with a.a(href='proyectos/Proyecto_' + str(id) + '.html', target='_blank'):
                                        a('&#9642 ' + proyecto[0])
                    with a.div(klass="text-center"):
                        with a.a(href="#desc", klass="btn btn-outline-secondary", type="button"):
                            a("Ver Categorías")
                    a.br()
                    a.br()
                    with a.dt(id="psebt"):
                        a('PRODUCTOS O SERVICIOS PARA EMPRENDIMIENTO DE BASE TECNOLOGICA')
                        for id, proyecto in psebt.items():
                            with a.dd():
                                if proyecto[1]:
                                    with a.a(href='proyectos/Proyecto_' + str(id) + '.html', target='_blank'):
                                        a('&#9642 ' + proyecto[0] + ' &#8212;')
                                        with a.p(klass="badge badge-success"):
                                                a("Con Enfoque Social")
                                else:
                                    with a.a(href='proyectos/Proyecto_' + str(id) + '.html', target='_blank'):
                                        a('&#9642 ' + proyecto[0])
                    with a.div(klass="text-center"):
                        with a.a(href="#desc", klass="btn btn-outline-secondary", type="button"):
                            a("Ver Categorías")
                        
                    
                








               
    html_bytes = bytes(a)
    with open('indiceMuestraVirtual.html', 'wb') as f:
        f.write(bytes(html_bytes))
    

                            

    

  


def main():
    loadProjects()
    outputHTML()
    
    
main()

        
            

