#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

class formulario:
	
	def __init__(self):
		
		self.window = gtk.Window()
		self.window.set_title("Cadastro de Informações")
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_resizable(False)
		self.window.set_border_width(10)
		self.window.connect("destroy", gtk.main_quit)
		
		#VBox box vertical
		self.box = gtk.VBox(False, 0)
		#contener individuais
		self.nomebox = gtk.VBox(True, 0)
		self.emailbox = gtk.VBox(True, 0)
		self.telefonebox = gtk.VBox(True, 0)
		self.botoesbox = gtk.VBox(False, 0)
		
		#Label
		self.labelnome = gtk.Label("Nome: ")
		self.labelemail = gtk.Label("Email: ")
		self.labeltelefone = gtk.Label("Telefone: ")
		
		#Entry
		self.nometexto = gtk.Entry()
		self.emailtexto = gtk.Entry()
		self.telefonetexto = gtk.Entry()
		
		#botoes
		self.enviar = gtk.Button("Enviar", gtk.STOCK_OK)
		self.cancelar = gtk.Button("Sair", gtk.STOCK_CANCEL)
		self.cancelar.connect("clicked", gtk.main_quit)
		
		#colocando tudo na janela
		#nome
		self.nomebox.pack_start(self.labelnome, False, False)
		self.nomebox.pack_start(self.nometexto, False, False)
		#email
		self.emailbox.pack_start(self.labelemail, False, False)
		self.emailbox.pack_start(self.emailtexto, False, False)
		#telefone
		self.telefonebox.pack_start(self.labeltelefone, False, False)
		self.telefonebox.pack_start(self.telefonetexto, False, False)
		#botoes
		self.botoesbox.pack_start(self.enviar, False, False)
		self.botoesbox.pack_start(self.cancelar, False, False)
		
		#colocando Hbox na janela
		self.box.pack_start(self.nomebox)
		self.box.pack_start(self.emailbox)
		self.box.pack_start(self.telefonebox)
		self.box.pack_start(self.botoesbox)
		
		self.window.add(self.box)
				
		self.window.show_all()
		
	def main(self):
		
		gtk.main()
	
