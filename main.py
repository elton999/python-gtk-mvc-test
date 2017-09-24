#!/usr/bin/env python
# -*- coding: utf-8 -*-

import model
import view

class controle:

	def __init__(self):
		print "Criando janela"
		self.janela = view.formulario()
		self.banco = model.magenda()
		self.janela.enviar.connect("clicked", self.inserir_contatos, None)

		self.janela.main()

	def inserir_contatos(self, banco, janela):
		print "Preparando dados..."
		self.banco.setNome(self.janela.nometexto.get_text())
		self.banco.setEmail(self.janela.emailtexto.get_text())
		self.banco.setTelefone(self.janela.telefonetexto.get_text())
		print "Inserindo dados..."
		self.banco.insert()
		

if __name__ == "__main__":
	
	c = controle()
