CREATE DATABASE LANCAMENTOSCONTABEIS;
USE LANCAMENTOSCONTABEIS;

CREATE TABLE Conta (
  conta_id INTEGER UNSIGNED NOT NULL,
  descricao VARCHAR(50) NOT NULL,
  PRIMARY KEY(id)
);

CREATE TABLE Lancamento (
  lancamento_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  data_registro DATE NOT NULL,
  contaDebito_id INTEGER UNSIGNED NOT NULL,
  contaCredito_id INTEGER UNSIGNED NOT NULL,
  valor DECIMAL(19,2) NOT NULL,
  historico VARCHAR(200) NOT NULL,
  PRIMARY KEY(lancamento_id),
  FOREIGN KEY(contaDebito_id) references Conta(conta_id),
  FOREIGN KEY(contaCredito_id) references Conta(conta_id),
  CONSTRAINT check_contas_diferentes CHECK(contaDebito_id <> contaCredito_id),
  CONSTRAINT valor_maior_zero CHECK(valor > 0)
);