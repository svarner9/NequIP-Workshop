import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')

df = pd.read_csv('./example/metrics_epoch.csv')
df

print('model: ', len(df), rf'{1000*df["validation_psavg_f_mae"].iloc[-1]:.2f}', rf'{1000*df["validation_e/N_mae"].iloc[-1]:.3f}')

# Plot training_loss_f and validation_loss_f
plt.figure()
plt.semilogy(df['epoch'], df['training_loss_f'], label='training_loss_f')
plt.semilogy(df['epoch'], df['validation_loss_f'], label='validation_loss_f')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.savefig('force_loss.png',dpi=200)

# Plot training_loss_e and validation_loss_e
plt.figure()
plt.semilogy(df['epoch'], df['training_loss_e'], label='training_loss_e')
plt.semilogy(df['epoch'], df['validation_loss_e'], label='validation_loss_e')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.savefig('energy_loss.png',dpi=200)

# Plot training_f_mae and validation_f_mae
plt.figure()
plt.semilogy(df['epoch'], df['training_f_mae'], label='training_f_mae')
plt.semilogy(df['epoch'], df['validation_f_mae'], label='validation_f_mae')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.savefig('force_mae.png',dpi=200)

# Plot training_e_mae and validation_e_mae
plt.figure()
plt.semilogy(df['epoch'], df['training_e_mae'], label='training_e_mae')
plt.semilogy(df['epoch'], df['validation_e_mae'], label='validation_e_mae')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.savefig('energy_mae.png',dpi=200)

# Plot training_loss and validation_loss
plt.figure()
plt.semilogy(df['epoch'], df['training_loss'], label='training_loss')
plt.semilogy(df['epoch'], df['validation_loss'], label='validation_loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.savefig('total_loss.png',dpi=200)

plt.close('all)
