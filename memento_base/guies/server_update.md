<!-- TOC INICIO -->
- [ERP](#erp)
  - [UPDATE](#update)
  - [ERRORS](#errors)
    - [BACKUP](#backup)
<!-- TOC FIN -->

# ERP

## UPDATE



## ERRORS

### BACKUP

Al fer un backup de la BDD d'un servidor abans d'actualitzar ERP, des de usuari erp pot aparèixer l'error:

```bash
pg_dump: error: query failed: ERROR:  permission denied for schema topology                              
pg_dump: error: query was: LOCK TABLE topology.topology IN ACCESS SHARE MODE
```

Cal accedir al psql amb usuari postgres, connectar-se a la base de dades de la qual es vol fer el backup i executar les següents commandes.

```bash
GRANT USAGE ON SCHEMA topology TO erp;
GRANT SELECT, USAGE ON ALL SEQUENCES IN SCHEMA topology to erp;
GRANT SELECT ON ALL TABLES IN SCHEMA topology to erp;
```