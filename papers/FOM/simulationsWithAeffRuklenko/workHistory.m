10.^(-[3.6 3.4 3.1]/2)./10.^(([7.5 14 9]-30)/10)./([9.14 15.2 8.34]*1e-3)
load aSiTM-12simulationData.txt
hold on
plot(aSiTM_12simulationData(:,1),aSiTM_12simulationData(:,2))
plot(aSiTM_12simulationData(1,:),aSiTM_12simulationData(2,:))
load aSiTM-12simulationFit.txt
plot(aSiTM_12simulationFit(1,:),aSiTM_12simulationFit(2,:))
hold on
plot(aSiTM_12simulationData(3,:),aSiTM_12simulationData(4,:))
plot(aSiTM_12simulationFit(3,:),aSiTM_12simulationFit(4,:))
hold on
load tm-6FiguresOfMeritsimulationData.txt
load tm-6FiguresOfMeritsimulationFit.txt
plot(tm_6FiguresOfMeritsimulationData(1,:),tm_6FiguresOfMeritsimulationData(2,:))
plot(tm_6FiguresOfMeritsimulationFit(1,:),tm_6FiguresOfMeritsimulationFit(2,:))
hold on
plot(tm_6FiguresOfMeritsimulationData(3,:),tm_6FiguresOfMeritsimulationData(4,:))
plot(tm_6FiguresOfMeritsimulationFit(3,:),tm_6FiguresOfMeritsimulationFit(4,:))
hold on
load te2wFiguresOfMeritsimulationData.txt
load te2wFiguresOfMeritsimulationFit.txt
hold on
plot(te2wFiguresOfMeritsimulationData(1,:),te2wFiguresOfMeritsimulationData(2,:))
plot(te2wFiguresOfMeritsimulationFit(1,:),te2wFiguresOfMeritsimulationFit(2,:))
hold on
plot(te2wFiguresOfMeritsimulationData(3,:),te2wFiguresOfMeritsimulationData(4,:))
plot(te2wFiguresOfMeritsimulationFit(3,:),te2wFiguresOfMeritsimulationFit(4,:))
saveFigure('timeRes_simulations_AmorfoTm10mmP13b_0p5w_SOI_2w__new')
