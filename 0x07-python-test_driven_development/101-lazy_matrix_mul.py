#!/usr/bin/python3
"""Defines a function that multiplies two matrices."""
import numpy as n


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices."""

    return (n.matmul(m_a, m_b))
