import React, {Component} from 'react';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Title from './Title';

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
    const newRows = [
      this.createData(0, '14:45, 16 Mar 2020', 'Módulo de Monitoreo', 'Módulo de Optimización', 'Si'),
      this.createData(1, '14:30, 16 Mar 2020', 'Módulo de Monitoreo', 'Módulo de Optimización', 'No'),
      this.createData(2, '14:15, 16 Mar 2020', 'Módulo de Monitoreo', 'Módulo de Optimización', 'No'),
      this.createData(3, '14:00, 16 Mar 2020', 'Módulo de Monitoreo', 'Módulo de Optimización', 'No'),
      this.createData(4, '13:45, 16 Mar 2020', 'Módulo de Monitoreo', 'Módulo de Optimización', 'Si'),
      this.createData(5, '13:30, 16 Mar 2020', 'Módulo de Monitoreo', 'Módulo de Optimización', 'No'),
      this.createData(6, '13:15, 16 Mar 2020', 'Módulo de Monitoreo', 'Módulo de Optimización', 'Si'),
      this.createData(7, '13:00, 16 Mar 2020', 'Módulo de Monitoreo', 'Módulo de Optimización', 'No'),
      this.createData(8, '12:45, 16 Mar 2020', 'Módulo de Monitoreo', 'Módulo de Optimización', 'No'),
      this.createData(9, '12:30, 16 Mar 2020', 'Módulo de Monitoreo', 'Módulo de Optimización', 'Si'),
    ];

    this.setState({
      rows: newRows
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