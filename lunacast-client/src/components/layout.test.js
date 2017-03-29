import React from 'react';
import { shallow } from 'enzyme';
import Layout from './layout';

describe('Layout', () => {

  it('renders children', () => {
    expect(shallow(
      <Layout>
        <div className="expected-class"></div>
      </Layout>
    ).find('.expected-class').length).toBe(1)
  });

});