import MySQLdb

class magenda:
    
    __nome = None
    __email = None
    __telefone = None

    #banco de dados
    def conectar(self):
        conn = MySQLdb.connect("localhost", "usuario", "senha", "banco")
        return conn
    
    #sets
    def setNome(self, nome):
        self.__nome = nome

    def setEmail(self, email):
        self.__email = email
    
    def setTelefone(self, telefone):
        self.__telefone = telefone

    #gets
    def getNome(self):
        return self.__nome

    def getEmail(self):
        return self.__email
    
    def getTelefone(self):
        return self.__telefone

    #inserir dados
    def insert(self):
        self.conn = self.conectar()
        self.cursor = self.conn.cursor()
        self.sql = "INSERT INTO contatos VALUES(null, '%s', '%s', '%s')" %(self.getNome(), self.getEmail(), self.getTelefone())
        
        try:
            self.cursor.execute(self.sql)
            self.conn.commit()
            print "Dados inseridos com sucesso\n"
            print "================================================================================\n"
        except:
            print "ERRO: ocorreu um erro durante a execucao"
