#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:00:29 2022

@author: fernandasanchez
"""

import pandas as pd
from airium import Airium



class Project:
  def __init__(self, id, name, description, category, img1, img2, img3, img4, img5, contact, videolink):
    self.id = id
    self.name = name
    self.description = description
    self.category = category
    self.img1 = img1
    self.img2 = img2
    self.img3 = img3
    self.img4 = img4
    self.img5 = img5
    self.contact = contact
    self.videolink = videolink

projects = []


def loadProjects():

    registrados = 'proyectos registrados final 2-11-2021.xlsx'
    muestra = 'info muestravirtual final 2-12-2021.xlsx'
    sheet =  0
    
    r = pd.read_excel(io=registrados, sheet_name=sheet)
    m = pd.read_excel(io=muestra,sheet_name=sheet)
    for index, row in r.iterrows():
        if row['ACCEPTADO'] == 'AC':
            id = row['ID']
            name = row['NOMBRE DEL PROYECTO']
            description = row['DESCRIPCION']
            category = row['TIPO DE PROYECTO']
            imgs = m.loc[m['PARENTID'] == id]
            img1 = imgs['PIC1NOM']
            img2 = imgs['PIC2NOM']
            img3 = imgs['PIC3NOM']
            img4 = imgs['PIC4NOM']
            img5 = imgs['PIC5NOM']
            contact = imgs['CONTACTO']
            videolink = imgs['VIDEOURL']
            temp = Project(id, name, description, category, img1.str.cat(sep='\n'), img2.str.cat(sep='\n'), img3.str.cat(sep='\n'), img4.str.cat(sep='\n'), img5.str.cat(sep='\n'), contact.str.cat(sep='\n'), videolink.str.cat(sep='\n'))
            projects.append(temp)          

    


def writeHTML():
    for p in projects:
        a = Airium()
        a('<!DOCTYPE html>')
        with a.html(lang="pl"):
            with a.head():
                a.meta(charset="utf-8")
                #<meta name="viewport" content="width=device-width, initial-scale=1">
                a.meta(name='viewport', content='width=device-width, initial-scale=1')
                a.title(_t="Muestra Virtual")
                a.link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css')
                a.link(rel='stylesheet', href='../assets/css/projects.css')
                a.link(rel='preconnect', href='https://fonts.googleapis.com')
                a.link(rel='preconnect', href='https://fonts.gstatic.com')
                a.link(href='https://fonts.googleapis.com/css2?family=Raleway:wght@200&display=swap', rel='stylesheet')
                a.link(href='<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&display=swap" rel="stylesheet">')
                a.link(rel='icon', href='assets/img/Screen Shot 2022-04-03 at 17.10.51.png')
                bgimg = '../fotos_proyectos/Proyecto_' + str(p.id) + '/' + str(p.img4)
            with a.body(style='background-image:url(' + str(bgimg) + ')'):
                with a.div(klass='container-fluid px-5 pb-5'):
                    with a.div(klass='row pt-2'):
                        with a.div(klass="col-lg-10"):
                            with a.h4():
                                a(p.category)
                            with a.h1():
                                a(p.name)
                        with a.div(klass='col-lg-2 text-center'):
                                a.img(src='../fotos_proyectos/Proyecto_' + str(p.id) + '/' + str(p.img1), width='100px', onerror="this.style.display='none'")
                    with a.div(klass="row pt-3"):
                        with a.div(klass='col-lg-12'):
                            with a.p():
                                a(p.description)
                    with a.div(klass='row pt-2', id='images'):
                        with a.div(klass='col-lg-4  my-auto text-center '):
                            a.img(klass='project-img', src='../fotos_proyectos/Proyecto_' + str(p.id) + '/' + str(p.img2))
                        with a.div(klass='col-lg-4  my-auto text-center '):
                            a.img(klass='project-img', src='../fotos_proyectos/Proyecto_' + str(p.id) + '/' + str(p.img3))
                        with a.div(klass='col-lg-4  my-auto text-center'):
                            a.img(klass='project-img', src='../fotos_proyectos/Proyecto_' + str(p.id) + '/' + str(p.img5))
                    with a.div(klass='row pt-3 text-center', id='video'):
                        with a.div(klass='col-lg-12'):
                            with a.a(klass='btn btn-primary', href=p.videolink):
                                a('Ver Video')
                    with a.div(klass='row pt-3', id='contact-info'):
                        with a.div(klass='col-md-12'):
                            with a.h4():
                                a('Contacto')
                            with a.p():
                                a(p.contact)    
        html_bytes = bytes(a)
        with open('proyectos/Proyecto_' + str(p.id) + '.html', 'wb') as f:
            f.write(bytes(html_bytes))
    

def main():
    loadProjects()
    writeHTML()

    
    
main()

        
            

