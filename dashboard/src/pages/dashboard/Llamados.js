import React, { Component } from 'react';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Title from './Title';
import axios from 'axios';

class Llamados extends Component {
  constructor(props) {
    super(props);

    this.state = {
      rows: []
    };
  }

  // Genera el contenido de cada fila en llamados
  createData = (id, fecha, origen, destino, llamado) => {
    return { id, fecha, origen, destino, llamado };
  }

  componentDidMount() {
    const newRows = [];

    axios.get('http://54.90.124.184:8000/api/states/')
      .then(res => {

        var i = 0;
        for (let llamado in res.data) {
          
          if (res.data[i].state == 0) {
            newRows.push(this.createData(i, res.data[i].Date, 'Módulo de Monitoreo', 'Módulo de Optimización', 'Si'));
          } else {
            newRows.push(this.createData(i, res.data[i].Date, 'Módulo de Monitoreo', 'Módulo de Optimización', 'No'));
          }
          i++;
        }

        this.setState({
          rows: newRows
        });

      });

  }

  render() {
    return (
      <React.Fragment>
        <Title>Llamados: Monitoreo - Optimización</Title>
        <Table size="small">
          <TableHead>
            <TableRow>
              <TableCell>Fecha</TableCell>
              <TableCell>Origen</TableCell>
              <TableCell>Destino</TableCell>
              <TableCell>Llamado</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {this.state.rows.map((row) => (
              <TableRow key={row.id}>
                <TableCell>{row.fecha}</TableCell>
                <TableCell>{row.origen}</TableCell>
                <TableCell>{row.destino}</TableCell>
                <TableCell>{row.llamado}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </React.Fragment>
    );
  }
}

export default Llamados;